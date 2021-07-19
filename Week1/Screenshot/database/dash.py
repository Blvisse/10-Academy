import numpy as np
import pandas as pd
import streamlit as st
import altair as alt
from wordcloud import WordCloud
import plotly.express as px
from connection import db_execute_fetch
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="User Analysis", layout="wide")

def loadData():
    query = "select * tweetsinformation"
    df = db_execute_fetch(query, dbName="tweets", rdf=True)
    return df

def selectHashTag():
    df = loadData()
    hashTags = st.multiselect("choose combaniation of hashtags", list(df['hashtags'].unique()))
    if hashTags:
        df = df[np.isin(df, hashTags).any(axis=1)]
        st.write(df)

# def selectDay():
#     df = loadData()
#     day = st.multiselect("choose date of tweet", list(df['day'].unique()))
#     if day:
#         df = df[np.isin(df, day).any(axis=1)]
#         st.write(df)
# def selectHour():
#     df = loadData()
#     hour = st.multiselect("choose hour of tweet", list(df['hour'].unique()))
#     if hour:
#         df = df[np.isin(df, hour).any(axis=1)]
#         st.write(df)

def selectPolarity():
    df = loadData()
    score = st.multiselect("choose experience of tweet", list(df['Experience Score'].unique()))
    if score:
        df = df[np.isin(df, score).any(axis=1)]
        st.write(df)

def selectAuthor():
    df=loadData()
    auths=st.multiselect("choose user", list(df['MSISDN/Number'].unique()))
    if auths:
        df = df[np.isin(df, auths).any(axis=1)]
        st.write(df)
# def selectLocAndAuth():
#     df = loadData()
#     location = st.multiselect("choose Location of tweets", list(df['place'].unique()))
#     lang = st.multiselect("choose Language of tweets", list(df['lang'].unique()))

#     if location and not lang:
#         df = df[np.isin(df, location).any(axis=1)]
#         st.write(df)
#     elif lang and not location:
#         df = df[np.isin(df, lang).any(axis=1)]
#         st.write(df)
#     elif lang and location:
#         location.extend(lang)
#         df = df[np.isin(df, location).any(axis=1)]
#         st.write(df)
#     else:
#         st.write(df)

def barChart(data, title, X, Y):
    title = title.title()
    st.title(f'{title} Chart')
    msgChart = (alt.Chart(data).mark_bar().encode(alt.X(f"{X}:N", sort=alt.EncodingSortField(field=f"{Y}", op="values",
                order='ascending')), y=f"{Y}:Q"))
    st.altair_chart(msgChart, use_container_width=True)


# def stBarChart():
#     df = loadData()
#     dfCount = pd.DataFrame({'Tweet_count': df.groupby(['original_author'])['original_text'].count()}).reset_index()
#     dfCount["original_author"] = dfCount["original_author"].astype(str)
#     dfCount = dfCount.sort_values("Tweet_count", ascending=False)

#     num = st.slider("Select number of Rankings", 0, 50, 5)
#     title = f"Top {num} Ranking By Number of tweets"
#     barChart(dfCount.head(num), title, "original_author", "Tweet_count")

# def hashTags():
#     df=loadData()
    
#     plt.figure(figsize=(10,8));
#     sns.color_palette("cubehelix", as_cmap=True)
#     sns.countplot(y=df['hashtags'],order=df['hashtags'].value_counts()[:10].index,palette='cubehelix')
#     plt.title("Most used hashtags")
#     plt.xticks(rotation=90);
    
# def langPie():
#     df = loadData()
#     dfLangCount = pd.DataFrame({'Tweet_count': df.groupby(['lang'])['original_text'].count()}).reset_index()
#     dfLangCount["lang"] = dfLangCount["lang"].astype(str)
#     dfLangCount = dfLangCount.sort_values("Tweet_count", ascending=False)
#     dfLangCount.loc[dfLangCount['Tweet_count'] < 10, 'lang'] = 'Other languages'
#     st.title(" Tweets Language pie chart")
#     fig = px.pie(dfLangCount, values='Tweet_count', names='lang', width=500, height=350)
#     fig.update_traces(textposition='inside', textinfo='percent+label')

#     colB1, colB2 = st.beta_columns([2.5, 1])

#     with colB1:
#         st.plotly_chart(fig)
#     with colB2:
#         st.write(dfLangCount)


st.title("Data Display")
# selectHashTag()
selectAuthor()

selectPolarity()
st.markdown("<p style='padding:10px; background-color:#000000;color:#00ECB9;font-size:16px;border-radius:10px;'>Section Break</p>", unsafe_allow_html=True)

# st.title("Data Visualizations")
# wordCloud()
# hashTags()


with st.beta_expander("Show More Graphs"):
    stBarChart()
    langPie()
    
{"mode":"full","isActive":false}