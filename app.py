import streamlit as st
st.set_page_config(page_title='Explore Your Music Taste', layout="wide")
import data
data.load_data()
from pages import overview, dataset, popularity, lyrics, audio, recommendation

st.sidebar.title("Explore Your Music Taste")
st.sidebar.write("Intro... ")
option = st.sidebar.selectbox(
    'Please choose the category you want to explore:',
    ('Overview', 'Dataset', 'Popularity', 'Song Lyrics', 'Audio Features', 'Song Recommendation'))

if option == "Overview":
    overview.page()

elif option == "Dataset":
    dataset.page()

elif option == "Popularity":
    popularity.page()

elif option == "Song Lyrics":
    lyrics.page()

elif option == "Audio Features":
    audio.page()

elif option == "Song Recommendation":
    recommendation.page()
