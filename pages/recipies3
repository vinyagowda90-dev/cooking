import streamlit as st
import pandas as pd
import plotly.express as px
from collections import Counter

from utils.data_loader import load_data

df = load_data()

st.title("🥘 Ingredient Analytics")

all_ingredients = []

for ingredients in df["ingredients"].dropna():

    items = str(ingredients).split(",")

    all_ingredients.extend(items)

counter = Counter(all_ingredients)

top20 = pd.DataFrame(
    counter.most_common(20),
    columns=[
        "Ingredient",
        "Count"
    ]
)

fig = px.bar(
    top20,
    x="Count",
    y="Ingredient",
    orientation="h",
    title="Top Ingredients"
)

st.plotly_chart(
    fig,
    use_container_width=True
)
