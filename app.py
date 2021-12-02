import streamlit as st
st.set_page_config(page_title='Explore Your Music Taste', layout="wide")
import data
data.load_data()
from pages import popularity, lyrics, audio

st.sidebar.title("Explore Your Music Taste")
st.sidebar.write("Intro... ")
option = st.sidebar.selectbox(
    'Please choose the category you want to explore:',
    ('Popularity', 'Song Lyrics', 'Audio Features'))

if option == "Popularity":
    popularity.page()


elif option == "Song Lyrics":
    lyrics.page()


elif option == "Audio Features":
    audio.page()
