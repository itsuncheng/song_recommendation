import streamlit as st
st.set_page_config(page_title="Explore Your Music Taste", layout="wide")
import data
data.load_data()
from pages import overview, dataset, popularity, lyrics, audio, recommendation


st.sidebar.title("**Welcome to Your Music Discovery Journey!**")

st.markdown('##')

option = st.sidebar.radio(
    'Please choose the category you want to explore:',
    ('About', 'Dataset', 'Popularity Analysis', 'Song Lyrics Analysis', 'Audio Features Analysis', \
    'Song Recommendation'))

if option == 'About':
    overview.page()

elif option == "Dataset":
    dataset.page()

elif option == "Popularity Analysis":
    popularity.page()

elif option == "Song Lyrics Analysis":
    lyrics.page()

elif option == "Audio Features Analysis":
    audio.page()

elif option == "Song Recommendation":
    recommendation.page()
