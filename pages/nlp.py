import streamlit as st

from wordcloud import WordCloud
import matplotlib.pyplot as plt

from utils.data_loader import load_data

df = load_data()

st.title("☁ NLP Insights")

text = " ".join(
    df["title"]
    .dropna()
    .astype(str)
)

wordcloud = WordCloud(
    width=1000,
    height=500
).generate(text)

fig, ax = plt.subplots()

ax.imshow(wordcloud)

ax.axis("off")

st.pyplot(fig)
