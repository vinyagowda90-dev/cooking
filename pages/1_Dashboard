import streamlit as st
import pandas as pd
from utils.data_loader import load_data

df = load_data()

st.title("📊 Dashboard")

col1,col2,col3 = st.columns(3)

col1.metric(
    "Total Recipes",
    len(df)
)

col2.metric(
    "Recipe Sources",
    df["source"].nunique()
)

col3.metric(
    "Columns",
    len(df.columns)
)

st.dataframe(df.head())
