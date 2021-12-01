import streamlit as st
import pandas as pd
from pages import popularity, lyrics, audio

st.sidebar.title("Explore Your Music Taste")
st.sidebar.write("Intro... ")
st.sidebar.write("Please choose the category you want to explore:")
option = st.sidebar.selectbox(
    'Select the info to check about',
    ('Popularity', 'Song Lyrics', 'Audio Features'))

if option == "Popularity":
    popularity.page()


elif option == "Song Lyrics":
    lyrics.page()


elif option == "Audio Features":
    audio.page()
