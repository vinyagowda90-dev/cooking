import streamlit as st
from utils.data_loader import load_data

df = load_data()

st.title("🔍 Recipe Search")

query = st.text_input(
    "Search Recipe"
)

if query:

    result = df[
        df["title"]
        .astype(str)
        .str.contains(
            query,
            case=False,
            na=False
        )
    ]

    st.write(
        f"Found {len(result)} recipes"
    )

    st.dataframe(result.head(20))
