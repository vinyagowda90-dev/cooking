import streamlit as st

from utils.data_loader import load_data
from utils.recommendation import (
    build_model,
    recommend
)

df = load_data()

st.title(
    "🤖 Recipe Recommendation"
)

similarity = build_model(df)

recipe = st.selectbox(
    "Select Recipe",
    df["title"].dropna().unique()
)

if st.button("Recommend"):

    recs = recommend(
        recipe,
        df,
        similarity
    )

    if recs is not None:

        st.dataframe(
            recs[["title"]]
        )
