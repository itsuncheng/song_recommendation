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
from PIL import Image


def page():
    ## Add title image
    title_image = Image.open("./images/title_img.jpg")
    st.image(title_image)

    
    title = "About"
    st.title(title)

    content1 = "<p style='color:Black; font-size: 20px;'>Music has become an integral part in almost everyone's daily life. We listen to music on \
    parties, while in commute, or relaxing at home. Music helps us relieve ourselves from stress, express \
    ourselves, or recharge us for the next day. However, have you ever explored music to a more profound \
    level? For example, have you ever wondered how different music genres differ from one another in terms of \
    audio features? What music genres do you like and why?</p>"
    st.markdown(content1,unsafe_allow_html=True)
    
    content2 = "<p style='color:Black; font-size: 20px;'>As data scientists and music lovers, our group is excited to perform some analysis over music. \
    We used a publicly online dataset from Kaggle to answer several reseach questions related to different dimensions of music data. We invite \
    you to explore what's popping in the music world and discover your music taste!"
    st.markdown(content2,unsafe_allow_html=True)
    st.markdown("Dataset: [Spotify and Genius Track Dataset](https://www.kaggle.com/saurabhshahane/spotgen-music-dataset)")








    
