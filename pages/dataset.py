import streamlit as st
import data
import pandas as pd
import altair as alt
import numpy as np
import pydeck as pdk
import matplotlib.pyplot as plt
import numpy as np
import sys
import seaborn as sns
from plotly.subplots import make_subplots
import plotly.express as px
import plotly.graph_objects as go

def page():
    st.set_option('deprecation.showPyplotGlobalUse', False)

    title = "Dataset"
    st.title(title)
    st.write("This application uses the \
    [Spotify and Genius Track Dataset](https://www.kaggle.com/saurabhshahane/spotgen-music-dataset) from Kaggle. \
    The original source of this dataset is provided by Spotify’s music API. This dataset contains \
    information on thousands of albums, artists, and tracks that are on \
    the Spotify platform. In addition, the dataset also contains lower-level audio features of the tracks, \
    as well as song lyrics. However, due to the huge dataset size, we have to select a portion of data from this \
    dataset to perform analysis. We leverage this sampled dataset for our project to conduct data analyses \
    and showcase this Streamlit application.")

    df = data.track_artist_album_df
    df = df[df['release_year'] > 1920]

    st.subheader("Basic Information")
    st.write("Below summarizes the key attributes of our sampled dataset.")
    info = [ ('101938'), ('75503'), ('40734'), ('11'), ('9'), ('4 min 7 sec')]
    new_df = pd.DataFrame(info, columns = ['Value'], index=["# tracks", "# albums", "# artists", "# genres", "# audio features", "average track duration"])
    st.table(new_df)

    st.subheader("Genre Distribution")
    st.write("The following plot shows all the genres from our selected dataset.")
    genre = data.track_with_genre_df
    fig = make_subplots(rows=1, cols=1,specs=[[{"type": "pie"}]])
    #data for pie
    pie_data = genre.groupby('genres')['id'].count()

    fig.add_trace(go.Pie(labels = pie_data.index,
                            values = pie_data.values,
                            hole = 0.4,
                            legendgroup = 'grp1',
                            showlegend=True),
                row = 1, col = 1)
    
    fig.update_traces(hoverinfo = 'label+percent',
                        textinfo = 'value+percent',
                        textfont_color = 'white',
                        marker = dict(line=dict(color='white', width=1)),
                        row = 1, col = 1)   
    
    st.write(fig)

    st.subheader("Track Release Year Distribution")
    st.write("Below shows the distribution of tracks in release year. From the histogram, we can see \
    that most tracks are released in the 21st century on Spotify. This is expected since technology is not \
    advanced back in the 21st century and many tracks are not well-documented compared to modern time. \
    Though the release time is not balanced enough, this does not interfere with our analysis since we can \
    still analzye tracks ranging for more than 20 years, which is still a long timespan.")
    
    fig = px.histogram(df, "release_year", nbins=30, title = "Number of Songs Released in Each Year in the Dataset")
    st.plotly_chart(fig)

    st.subheader("Track Duration Distribution")
    st.write("Below shows the distribution of track duration. From the plot, we can see that more \
    than 90 percent of tracks have duration less than 5 minutes.")
    df = df.rename(columns={'duration_sec': 'duration'})
    fig = px.ecdf(df, "duration", title = "Track Duration Distribution")
    st.plotly_chart(fig)

    # st.subheader("Data Quality")

    # st.markdown("**Completeness**")
    # st.write("The dataset is relatively complete, as this dataset is directly retrieved from the Spotify \
    # API. Although we perform some sampling and cleaning so that the application can successfully run, all rows \
    # have complete data and does not interfere with our analysis.")

    # st.markdown("**Coherency**")
    # st.write("...")

    # st.markdown("**Corretness**")
    # st.write("...")

    # st.markdown("**Accountability**")
    # st.write("...")
