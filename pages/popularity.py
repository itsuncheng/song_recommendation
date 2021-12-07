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
import plotly.express as px

genre_names = ['Dance Pop', 'Electronic', 'Electropop', 'Hip Hop', 'Jazz', 'K-pop', 'Latin', 'Pop', 'Pop Rap', 'R&B', 'Rock']

def page():
    # TODO: Popularity Page
    st.title("What's Trending in the World and Why?")
    st.write("As music becomes integral in people's life, \
    the music industry has grown to an exceptional level to satisfy people's demand. As more and more music tracks are \
    being produced, some tracks are more popular than others by comparing the number of views. \
    For example, the song \"Love Yourself\" by Justin Bieber is much more popular than the song \
    \"New York City\" by Owl City. However, have you ever wondered what factors affect this difference in \
    popularity? In this section, we would like to investigate the factors that affect a track's popularity. \
    In this dashboard we present different factors as well as their corresponding change with popularity. We \
    focus on time, audio features, and artists.")
    
    st.header("Genres")
    st.write("Is a particular genre more popular than another? How does people's taste change over time? In this section,\
            you will be able to explore that with the visualization below. Feel free to add genres you would like to learn more about\
            and see how its popularity evolves over time!")

    genre_options = st.multiselect('Which genres would you like to select',
    genre_names, ["Pop", "Hip Hop", "K-pop"])

    lowered_genre_options = [f.lower() for f in genre_options]
    exploded_track_df = data.exploded_track_df
    filtered_df = exploded_track_df[exploded_track_df["genres"].isin(lowered_genre_options)]
    grouped_df = filtered_df.groupby(["genres", "release_year"]).agg({"popularity" : "mean"})
    grouped_df = grouped_df.add_suffix('').reset_index()
    fig = px.line(grouped_df, x="release_year", y="popularity", color='genres')
    fig.update_layout(title_text="Popularity of Genres throughout Time")
    st.plotly_chart(fig, use_container_width=True)

    st.header("Top 10 Songs and Artists")
    st.write("""Who are the artists of the year? Which songs top the chart? We displayed the top artists \
              and top songs below from each year. Check out if your favorite artists/songs made their way to the Spotify TOP 10!""")

    year_selected = st.slider("Select the year", 1990, 2019, 2019)
    top_10_songs = filtered_df[filtered_df["release_year"]==year_selected].sort_values(by=['popularity'], ascending=False)["name"].unique()[:10]
    top_10_artists = filtered_df[filtered_df["release_year"]==year_selected].sort_values(by=['popularity'], ascending=False)["artists_name"].unique()[:10]
    
    d = {'Top Songs': top_10_songs, 'Top Artists': top_10_artists}
    df = pd.DataFrame(data=d)
    df.index = list(range(1, 11))
    st.table(df)



    st.header("Audio Features")
    st.write("Spotify measures the audio characteristics of a song by audio features. These audio features describe the differences \
            in songs. One may want to ask the question: can the audio features be tied to the popularity of a song and do artists \
            tend to release certain types of songs over the years? You can use the three plots below to help answer these questions.\
            We will discuss audio features more in the audio feature analysis tab. If you want to learn more about what each audio feature \
            means, please go to the audio feature analysis tab and scroll down to the bottom!")
    st.markdown("Audio features we will be exploring here are acousticness, danceability, duration_sec, energy, instrumentalness, key, liveness, loudness, speechiness, tempo, and time_signature. Time_signature is a measure of beats per minute of tracks.")
    df = data.track_artist_album_df


    option = st.selectbox('Which audio feature would you like to explore?',
    ('acousticness', 'danceability', 'duration_sec', 'energy', 'instrumentalness', 'key',
        'liveness', 'loudness', 'speechiness', 'tempo','time_signature'))
    attributeTrack = df[[option, 'popularity']]
    attributeTrack = attributeTrack.groupby(option).mean().reset_index()
    # attributeTrack.rename(columns={'popularity': option+" "}, inplace=True)
    chart = alt.Chart(attributeTrack).mark_line().encode(
        x=alt.X(option+':Q'),
        y=alt.Y('popularity:Q'),
        ).properties(title="Change in popularity with respect to " + option)
    st.altair_chart(chart, use_container_width=True)
  

    


    attributeTime = df[[option, 'popularity', 'release_year']]
    yearArr = pd.unique(attributeTime['release_year'])
    attributeTimeAll = attributeTime.groupby('release_year')
    # df2 = pd.DataFrame( columns=[option, 'popularity', 'release_year'])
    df2 = pd.DataFrame()
    for group_name, df_group in attributeTimeAll:
        # group_name
        df_group = df_group.groupby(option).mean().reset_index()
        # df_group
        df2 = df2.append(df_group,ignore_index = True)
        
    # x-axis label to dense
    # chart = alt.Chart(df2).mark_circle(color = 'red', opacity=0.55).encode(
    #     x='release_year:N', y='popularity', color=option,tooltip=[option, 'popularity', 'release_year']
    #     ).properties(title="Change in popularity with respect to " + option + " by release years")
    # st.altair_chart(chart, use_container_width=True)
    # Data too sparse
    chart = alt.Chart(df2).mark_circle(color = 'red', opacity=0.55).encode(
        x=alt.X('release_year:Q',axis=alt.Axis(tickCount=len(yearArr)/10, grid=False),scale=alt.Scale(zero=False)), y='popularity', color=option,tooltip=[option, 'popularity', 'release_year']
        ).properties(title="Change in popularity with respect to " + option + " by release years")
    st.altair_chart(chart, use_container_width=True)




    attributeTime = attributeTime.sort_values(by=['release_year'], ascending = False)
    yearArr = np.append(yearArr, 'ALL years')
    # yearArr[0].type()
    options = st.multiselect(
        'Choose years to display',
        yearArr,['2019', '2018', '2017', '2016', '2015', '2014'])
    if 'ALL years' not in options :
        options = [int(x) for x in options]
        attributeTime = attributeTime[attributeTime['release_year'].isin(options)]
    attributeTime = attributeTime.groupby('release_year')
    # df2 = pd.DataFrame( columns=[option, 'popularity', 'release_year'])
    df2 = pd.DataFrame()
    for group_name, df_group in attributeTime:
        # group_name
        df_group = df_group.groupby(option).mean().reset_index()
        # df_group
        df2 = df2.append(df_group,ignore_index = True)
    chart = alt.Chart(df2).mark_line().encode(
    x=alt.X(option+':Q'),
    y=alt.Y('popularity:Q'),
    color='release_year:N',
    ).properties(title="Change in popularity with respect to " + option + " by release years")
    st.altair_chart(chart, use_container_width=True)