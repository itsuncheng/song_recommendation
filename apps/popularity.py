import streamlit as st
import pandas as pd
import altair as alt
import numpy as np
import pydeck as pdk
import matplotlib.pyplot as plt
import numpy as np
import sys
import seaborn as sns

def app():
    # TODO: Popularity Page
    st.title('What factors effect the popularity of a track?')
    st.write('In this dashboard we will analyze differenct factors as well as their corresponding change in popylarity. We focus on time, audio features, and artists.')

    df = pd.read_csv("../datasets/trackArtistAlblum.csv")


    option = st.selectbox('Which audio feature would you like to explore?',
    ('acousticness', 'danceability', 'duration_sec', 'energy', 'instrumentalness', 'key',
        'liveness', 'loudness', 'speechiness', 'tempo','time_signature'))
    attributeTrack = df[[option, 'popularity']]
    attributeTrack = attributeTrack.groupby(option).mean().reset_index()
    # attributeTrack.rename(columns={'popularity': option+" "}, inplace=True)
    chart = alt.Chart(attributeTrack).mark_line().encode(
        x=alt.X(option+':Q'),
        y=alt.Y('popularity:Q'),
        ).properties(title="Change in popularity with respect to " + option)
    st.altair_chart(chart, use_container_width=True)
  

    


    attributeTime = df[[option, 'popularity', 'release_year']]
    attributeTimeAll = attributeTime.groupby('release_year')
    # df2 = pd.DataFrame( columns=[option, 'popularity', 'release_year'])
    df2 = pd.DataFrame()
    for group_name, df_group in attributeTimeAll:
        # group_name
        df_group = df_group.groupby(option).mean().reset_index()
        # df_group
        df2 = df2.append(df_group,ignore_index = True)
    chart = alt.Chart(df2).mark_circle( opacity=0.2).encode(
        x='release_year:N', y='popularity', color=option,size = option,tooltip=[option, 'popularity', 'release_year']
        ).properties(title="Change in popularity with respect to " + option + " by release years")
    st.altair_chart(chart, use_container_width=True)




    attributeTime = attributeTime.sort_values(by=['release_year'], ascending = False)
    yearArr = pd.unique(attributeTime['release_year'])
    yearArr = np.append(yearArr, 'ALL years')
    # yearArr[0].type()
    options = st.multiselect(
        'Choose years to display',
        yearArr,['2019', '2018', '2017', '2016', '2015', '2014'])
    if 'ALL years' not in options :
        options = [int(x) for x in options]
        attributeTime = attributeTime[attributeTime['release_year'].isin(options)]
    attributeTime = attributeTime.groupby('release_year')
    # df2 = pd.DataFrame( columns=[option, 'popularity', 'release_year'])
    df2 = pd.DataFrame()
    for group_name, df_group in attributeTime:
        # group_name
        df_group = df_group.groupby(option).mean().reset_index()
        # df_group
        df2 = df2.append(df_group,ignore_index = True)
    chart = alt.Chart(df2).mark_line().encode(
    x=alt.X(option+':Q'),
    y=alt.Y('popularity:Q'),
    color='release_year:N',
    ).properties(title="Change in popularity with respect to " + option + " by release years")
    st.altair_chart(chart, use_container_width=True)


app()