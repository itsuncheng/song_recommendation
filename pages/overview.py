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


def page():
    title = "Overview"
    st.title(title)
    st.write("Music has become an integral part in almost everyone's daily life. We listen to music during \
    party, in transportation, or relaxing at home. Music helps us relieve ourselves from stress, express \
    ourselves, or give us energy for the next day. However, have you ever explored music to a more profound \
    level? For example, have you ever wondered how different music genre differ from one another in terms of \
    audio features? What music genres do you like and why?")

    st.write("As data scientists and music lovers, our group is excited to perform some analysis over music. \
    We would like to use the [Spotify and Genius Track Dataset](https://www.kaggle.com/saurabhshahane/spotgen-music-dataset) \
    publicly online to answer several reseach questions related to different dimensions of music data.")

    st.subheader("Popularity Analysis")
    st.write("The first research question focuses on popularity. As music becomes integral in people's life, \
    the music industry has grown to an exceptional level to satify people's demand. As more and more music tracks are \
    being produced, some tracks are more popular than others by comparing the number of views. \
    For example, the track \"Love Yourself\" by Justin Bieber is much more popular than the track \
    \"New York City\" by Owl City. However, have you ever wondered what factors affect this difference in \
    popularity? In this section, we would like to investigate the factors that affect a track's popularity. \
    Our research question is: ") 
    st.markdown("**What music features or artist features affect song popularity and by how much?**")

    st.subheader("Song Lyrics Analysis")
    st.write("Our second research question focuses on lyrics. The growth of music industry also implies the \
    growth in number of music genres, as more and more diverse tracks are being produced. The most common \
    genres include pop, rock, jazz, and etc that have been popular for a long time; however, genres like \
    k-pop is an increasing popular genre that have become mainstream genre for many listeners in the past decade. \
    For so many music genres, we start wondering how do the type of words differ in each genre. Intuition \
    tells us that certain genres use particular words that closely associate with that genre. \
    For instance, we might see the words \"love\" and \"dancing\" appear in the lyrics of dance pop more \
    frequently than other genres. To test our hypothesis and further understand the type of words used in each \
    genre, we focus on the following research question: ")
    st.markdown("**How do word usages compare across different genres?**")

    st.subheader("Audio Features Analysis")
    st.write("Our third research question focuses on audio features, spanning from accousticness, danceability, \
    duration, energy, instrumentalness, liveness, temp, and valence. After diving into word lyrics across \
    different music genres, we start wondering how other audio features differ in different music genres. \
    Again, intution tells us that certain genres have higher audio features than others; for example, \
    the audio feature danceability would have higher density in k-pop than in jazz. To test our hypothesis and \
    understand the audio features in each genre, we focus on the following research question: ")
    st.markdown("**What is the correlation between different audio features and the density of each audio feature \
    for each genre?**")

    st.subheader("Song Recommendation")
    st.write("Our final and the most exciting section focuses on song recommendation. After analyzing the music \
    genres through different dimensions, we would like to see what are the actual songs recommended by adjusting \
    different features we have investigated. This is the place, where you can verify whether the audio features \
    correctly reflect the song by listening to the track directly! For instance, you can switch to the genre \
    k-pop and increase danceability to maximum while keeping others constant and check whether the recommended \
    song indeed prompts you to dance and party! Our research question is then ...")
    st.markdown("**Do the audio features indeed reflect the song for each genre?**")



    
