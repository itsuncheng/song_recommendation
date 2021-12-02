## File for data loading purposes
## Please load all of the required data files here

import numpy as np
import pandas as pd

def load_genre_audio():
    global electronic
    global hippop
    global jazz
    global kpop
    global pop
    global randb
    global rock

    with open('data/audio/electronic.npy', 'rb') as f:
        electronic = np.load(f)
    with open('data/audio/hippop.npy', 'rb') as f:
        hippop = np.load(f)
    with open('data/audio/jazz.npy', 'rb') as f:
        jazz = np.load(f)
    with open('data/audio/kpop.npy', 'rb') as f:
        kpop = np.load(f)
    with open('data/audio/pop.npy', 'rb') as f:
        pop = np.load(f)
    with open('data/audio/randb.npy', 'rb') as f:
        randb = np.load(f)
    with open('data/audio/rock.npy', 'rb') as f:
        rock = np.load(f)

# @st.cache(allow_output_mutation=True)
def load_data():
    data_dir = "data/SpotGenTrack/Data Sources/"

    global albums_data
    global artists_data
    global tracks_data
    albums_data = pd.read_csv(data_dir+"spotify_albums.csv")
    artists_data = pd.read_csv(data_dir+"spotify_artists.csv")
    tracks_data = pd.read_csv(data_dir+"spotify_tracks.csv")

    load_genre_audio()
