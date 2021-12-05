import streamlit as st
import data


def page():
    title = "Visualize the Lyrics of Your Favorite Song"
    st.title(title)
    st.write("The growth of music industry also implies the \
    growth in number of music genres, as more and more diverse tracks are being produced. The most common \
    genres include pop, rock, jazz, and etc that have been popular for a long time; however, genres like \
    k-pop is an increasing popular genre that have become mainstream genre for many listeners in the past decade. \
    For so many music genres, we start wondering how do the type of words differ in each genre. Intuition \
    tells us that certain genres use particular words that closely associate with that genre. \
    For instance, we might see the words \"love\" and \"dancing\" appear in the lyrics of dance pop more \
    frequently than other genres. To test our hypothesis and further understand the type of words used in each \
    genre, we focus on the following research question: ")