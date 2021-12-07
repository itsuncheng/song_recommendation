import streamlit as st
import data
from wordcloud import WordCloud
from typing import List, Tuple
import pandas as pd
from matplotlib import pyplot as plt
import random
from annotated_text import annotated_text

genre_names = ['Dance Pop', 'Electronic', 'Electropop', 'Hip Hop', 'Jazz', 'J-pop', 'K-pop', 'Latin', 'Pop', 'Pop Rap', 'R&B', 'Rock']
lyric_sentiment= data.lyric_sentiments
lyric_knn = data.lyric_knn
cleaned_lyric = data.cleaned_lyric
song_sentiment = data.song_sentiments
songs = list(song_sentiment.keys())
songs_with_lyrics = data.exploded_track_df
songs_with_lyrics["lyric_length"]=[len(item.split(" ")) for item in songs_with_lyrics.lyrics]
songs_with_lyrics=songs_with_lyrics[songs_with_lyrics["lyric_length"]>5]

def generate_wordcloud(lyrics:List):
  """lyrics [List]: list of lyrics of all the songs
     return: A wordcloud object"""
  long_string = ",".join(lyrics)
  wc = WordCloud(background_color="white", max_words=75, contour_width=3, contour_color='steelblue',width=800, height=400)
  wc.generate(long_string)
  return wc

def plot_sentiment_distribution():
    df = pd.DataFrame(columns=('genre','Positive','Neutral',"Negative"))
    for i,genre in enumerate(lyric_sentiment):
        df.loc[i]=(genre, *lyric_sentiment[genre]["sentiment_distribution"])
    axs = df.plot.barh(x='genre', stacked=True )
    axs.set_title("Lyrics Sentiment Distribution among different Genres")
    plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))
    plt.show()
    st.pyplot(plt.gcf())

def get_lyrics(id):
    lyric = songs_with_lyrics[songs_with_lyrics["id"] == id]["lyrics"].item()
    return "\n".join(lyric.split("\n")[:10])

def get_sentiment_sentences(genre:str)->Tuple:
    """This functions returns 10 strong positive lyrics and 10 strong negative lyrics within selected genre"""
    return lyric_sentiment[genre]["positive_sentences"], lyric_sentiment[genre]["negative_sentences"]

def get_random_song():
    """Randomly select a song, retrun the word cloud corresponds to its lyrics and sentiments of each sentence"""
    song_name = random.choice(songs)
    wc, lyrics, sentiments = get_song_info(song_name)
    return song_name,wc, lyrics, sentiments

def get_song_info(song_name):
    lyrics = [item[0] for item in song_sentiment[song_name]]
    wc = generate_wordcloud(lyrics)
    sentiments = [item[1] for item in song_sentiment[song_name]]
    return wc, lyrics, sentiments


def format_lyric_with_sentiments(lyrics, sentiments):
    ret =[]
    for lyric, score in zip(lyrics, sentiments):
        if score>0.3:
            annotation = "Positive"
            lv=int(255*(1-score))
            color = "rgb({},255,{}".format(lv,lv)
        elif score < -0.3:
            annotation = "Negative"
            lv=int(255*(1-abs(score)))
            color ="rgb(255,{},{})".format(lv,lv)
        else:
            annotation = "Neutral"
            color ="rgb(255,255,255)"
        ret.append((lyric+"\n", annotation, color))
    return ret



def get_lyrics(id, N=10):
    """Get lyrics of a song given its unqiue id, return first N rows of the lyric"""
    lyric = songs_with_lyrics[songs_with_lyrics["id"] == id].iloc[0]["lyrics"]
    return "\n".join(lyric.split("\r\n")[:N])



def get_neighbors(lyric):
    pass
    #ToDO: Do we really need this since the result does not make much sense



def page():
    title = "Visualize word distribution and Analyze sentiment of the Lyrics in different Genres"
    st.title(title)
    st.subheader("Lets first look at the sentiment distribution over all the genres")

    plot_sentiment_distribution()


    st.write("The growth of music industry also implies the \
    growth in number of music genres, as more and more diverse tracks are being produced. The most common \
    genres include pop, rock, jazz, and etc that have been popular for a long time; however, genres like \
    k-pop is an increasing popular genre that have become mainstream genre for many listeners in the past decade. \
    For so many music genres, we start wondering how do the type of words differ in each genre. Intuition \
    tells us that certain genres use particular words that closely associate with that genre. \
    For instance, we might see the words \"love\" and \"dancing\" appear in the lyrics of dance pop more \
    frequently than other genres. To test our hypothesis and further understand the type of words used in each \
    genre, we focus on the following research question: ")


    genre = st.selectbox(label="Select One Genre",
                         options=genre_names)

    st.subheader("Words in {} Genre".format(genre))
    st.image(generate_wordcloud(cleaned_lyric[genre]).to_array())



    pos_sent, neg_sent = get_sentiment_sentences(genre)
    with st.container():
        col1, col2 = st.columns(2)
        with col1:

            st.subheader("10 typical strong positive lyric sentences in {} genre".format(genre))
            st.code("\n".join([item[0] for item in pos_sent]), language=None)
        with col2:
            st.subheader("10 typical strong negative lyric sentences in the {} genre".format(genre))
            st.code("\n".join(item[0] for item in neg_sent), language=None)
    songname = st.selectbox(label="Select a song!", options=songs)
    st.write("OR")
    clicked = st.button("Surprise me with a random song!")
    if clicked:
        songname, wc, lyrics, sentiments = get_random_song()
        st.write("Song name: {}".format(songname))
        st.subheader("Word Cloud of {}".format(songname))
        st.image(wc.to_array())
        st.subheader("Sentiments of {}'s lyrics".format(songname))
        annotated_text(*format_lyric_with_sentiments(lyrics, sentiments))

    elif songname:
        wc,lyrics,sentiments = get_song_info(songname)
        st.write("Song name: {}".format(songname))
        st.subheader("Word Cloud of {}".format(songname))
        st.image(wc.to_array())
        st.subheader("Sentiments of {}'s lyrics".format(songname))
        annotated_text(*format_lyric_with_sentiments(lyrics, sentiments))
















