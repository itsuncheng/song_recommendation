import streamlit as st
import data
import plotly.figure_factory as ff
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objs as go


genre_names = ['Dance Pop', 'Electronic', 'Electropop', 'Hip Hop', 'Jazz', 'K-pop', 'Latin', 'Pop', 'Pop Rap', 'R&B', 'Rock']

audio_feat_names = ['Acousticness', 'Danceability', 'Duration_ms',
                'Energy', 'Instrumentalness', 'Liveness',
                'Loudness', 'Speechiness', 'Tempo', 'Valence']

def plot_genre_distribution(selected_genres):

    fig = make_subplots(rows=5, cols=2)
    combined = [(f, s) for f in range(5) for s in range(2)]
    showLegend = True
    for n, (i, j) in enumerate(combined):
        hist_data = []
        for genre in selected_genres:
            genre = genre.lower()
            hist_data.append(data.genres2audio[genre][:, n])
        sub_fig = ff.create_distplot(hist_data, selected_genres, show_hist=False, show_rug=False)
        if n == 1:
            showLegend = False
        for b in range(len(sub_fig['data'])):
            fig.add_trace(go.Scatter(sub_fig['data'][b], showlegend=showLegend), row=i+1, col=j+1)

    for i in range(10):
        x_axis_str = "xaxis"
        y_axis_str = "yaxis"
        if i != 0:
            x_axis_str += str(i+1)
            y_axis_str += str(i+1)
        fig['layout'][x_axis_str]['title'] = audio_feat_names[i]
        fig['layout'][y_axis_str]['title'] = "Value"

    fig.update_layout(height=1200, width=800, title_text="Title")
    st.plotly_chart(fig, use_container_width=True)

def page():
    st.title('Why Do Genres Sound Different?')
    st.write("Have you ever wondered why \"Drivers License\" by Olivia Rodringo sound so differently from \"Savage Love\" by Jason Derulo?\
    In this section, we focus on audio features, spanning from accousticness, danceability, \
    duration, energy, instrumentalness, liveness, temp, and valence, which together characterize what a song sounds like. After diving into word lyrics across \
    different music genres, we start wondering how other audio features differ in different music genres. \
    Again, intuition tells us that certain genres have higher audio features than others; for example, \
    the audio feature danceability would have higher density in k-pop than in jazz. Hopefully this section can give you more insights into \
    which type of music/genre to vibe to at a Friday night party or a Saturday afternoon coffee break!")


    selected_genres = st.multiselect(
        'Select some genres',
        genre_names,
        ["Electronic", "Hip Hop", "Jazz", "K-pop", "Pop"])

    plot_genre_distribution(selected_genres)

    st.markdown("## To see what each feature means:")
    with st.expander("Expand below"):
    
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.subheader("Acousticness")
            st.markdown("A confidence measure from 0.0 to 1.0 of whether the "+
                        "track is acoustic. 1.0 represents high confidence the track is acoustic.")
            
            st.subheader("Liveness")
            st.markdown("Detects the presence of an audience in the recording. Higher liveness values "+
                        "represent an increased probability that the track was performed live. A value above 0.8 "+
                        "provides strong likelihood that the track is live.")
            
            st.subheader("Speechiness ")        
            st.markdown("Detects the presence of spoken words in a track. The more exclusively speech-like the "+
                "recording (e.g. talk show, audio book, poetry), the closer to 1.0 the attribute value. Values "+
                "above 0.66 describe tracks that are probably made entirely of spoken words. Values between 0.33 and"+
                "0.66 describe tracks that may contain both music and speech, either in sections or layered, including such"+
                "cases as rap music. Values below 0.33 most likely represent music and other non-speech-like tracks") 
            
        with col2:
            st.subheader("Danceability")
            st.markdown("Describes how suitable a track is for dancing based on a "+
                        "combination of musical elements including tempo, rhythm stability, beat strength, "+
                        "and overall regularity. A value of 0.0 is least danceable and 1.0 is most danceable.")
            
            st.subheader("Instrumentalness")
            st.markdown("Predicts whether a track contains no vocals. "+
                "“Ooh” and “aah” sounds are treated as instrumental in this context. "+
                "Rap or spoken word tracks are clearly “vocal”. The closer the instrumentalness "+
                "value is to 1.0, the greater likelihood the track contains no vocal content. Values "+
                "above 0.5 are intended to represent instrumental tracks, but confidence is higher as the "+
                "value approaches 1.0")
            
            st.subheader("Tempo")
            st.markdown("The overall estimated tempo of a track in beats per minute (BPM). In musical terminology, tempo is"+
                "the speed or pace of a given piece and derives directly from the average beat duration.")

        with col3:
            st.subheader("Energy")
            st.markdown("Energy is a measure from 0.0 to 1.0 and represents a perceptual measure of intensity "+
                        "and activity. Typically, energetic tracks feel fast, loud, and noisy."+
                        "For example, death metal has high energy, while a Bach prelude scores low on the scale. "+
                        "Perceptual features contributing to this attribute include dynamic range, perceived loudness, "+
                        "timbre, onset rate, and general entropy.")
            
            st.subheader("Loudness")
            st.markdown("The overall loudness of a track in decibels (dB). Loudness values are "+
                        "averaged across the entire track and are useful for comparing relative loudness "+
                        "of tracks. Loudness is the quality of a sound that is the primary psychological "+
                        "correlate of physical strength (amplitude). Values typical range between -60 and 0 db")
            
            st.subheader("Valence")
            st.markdown("A measure from 0.0 to 1.0 describing the musical positiveness conveyed by a track. "+
                "Tracks with high valence sound more positive (e.g. happy, cheerful, euphoric), while tracks with low"+
                "valence sound more negative (e.g. sad, depressed, angry).")
