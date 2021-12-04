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
    We would like to use [the Spotify and Genius Track Dataset](https://www.kaggle.com/saurabhshahane/spotgen-music-dataset) \
    publicly online to answer several reseach questions.")

    
