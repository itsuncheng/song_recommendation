import streamlit as st
from multiapp import MultiApp
from reference_apps import home, data, model  # import your app modules here
from apps import popularity, lyrics, audio

app = MultiApp()

st.markdown("""
# Multi-Page App

This multi-page app is using the [streamlit-multiapps](https://github.com/upraneelnihar/streamlit-multiapps) framework developed by [Praneel Nihar](https://medium.com/@u.praneel.nihar). Also check out his [Medium article](https://medium.com/@u.praneel.nihar/building-multi-page-web-app-using-streamlit-7a40d55fa5b4).

""")

# Add all your application here
# Reference apps
app.add_app("Home", home.app)
app.add_app("Data", data.app)
app.add_app("Model", model.app)

# Our apps
app.add_app("Popularity", popularity.app)
app.add_app("Lyrics", lyrics.app)
app.add_app("Audio Features", audio.app)

# Run our app
app.run()
