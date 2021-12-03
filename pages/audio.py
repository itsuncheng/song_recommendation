import streamlit as st
import data
import plotly.figure_factory as ff
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objs as go

genre_names = ['Anime', 'Dance Pop', 'Electronic', 'Electropop', 'Hip Hop', 'Jazz', 'J-pop', 'K-pop', 'Latin', 'Pop', 'Pop Rap', 'R&B', 'Rock']

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
    title = "Explore Various Audio Features"
    st.title(title)

    selected_genres = st.multiselect(
        'Select some genres',
        genre_names,
        ["Electronic", "Hip Hop", "Jazz", "K-pop", "Pop"])

    plot_genre_distribution(selected_genres)

