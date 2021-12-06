## File for data loading purposes
## Please load all of the required data files here
import streamlit as st
import numpy as np
import pandas as pd

@st.cache(allow_output_mutation=True)
def load_genre_audio():

    global exploded_track_df
    df = pd.read_csv("data/filtered_track_df.csv")
    df['genres'] = df.genres.apply(lambda x: [i[1:-1] for i in str(x)[1:-1].split(", ")])
    exploded_track_df = df.explode("genres")

    genres = ['dance pop', 'electronic', 'electropop', 'hip hop', 'jazz', 'k-pop', 'latin', 'pop', 'pop rap', 'r&b', 'rock']
    audio_feats = ['acousticness', 'danceability', 'duration_ms',
                    'energy', 'instrumentalness', 'liveness',
                    'loudness', 'speechiness', 'tempo', 'valence']

    global genres2audio
    genres2audio = {}
    for genre in genres:
        genres2audio[genre] = exploded_track_df[exploded_track_df["genres"]==genre][audio_feats].to_numpy()

@st.cache(allow_output_mutation=True)
def load_genre_artist():

    global exploded_artist_df
    data_dir = "data/SpotGenTrack/Data Sources/"
    df = pd.read_csv(data_dir+"spotify_artists.csv")
    df['genres'] = df.genres.apply(lambda x: [i[1:-1] for i in str(x)[1:-1].split(", ")])
    exploded_artist_df = df.explode("genres")

    genres = ['k-pop', 'rap']
    artist_feats = ['popularity']

    global genres2artist
    genres2artist = {}
    for genre in genres:
        genres2artist[genre] = exploded_artist_df[exploded_artist_df["genres"]==genre][artist_feats].to_numpy()


@st.cache(allow_output_mutation=True)
def load_track_artist_album():
    global track_artist_album_df
    track_artist_album_df = pd.read_csv("data/trackArtistAlbum.csv")

@st.cache(allow_output_mutation=True)
def load_data():
    # data_dir = "data/SpotGenTrack/Data Sources/"

    # global albums_data
    # global artists_data
    # global tracks_data
    # albums_data = pd.read_csv(data_dir+"spotify_albums.csv")
    # artists_data = pd.read_csv(data_dir+"spotify_artists.csv")
    # tracks_data = pd.read_csv(data_dir+"spotify_tracks.csv")

    load_genre_audio()
    load_track_artist_album()
