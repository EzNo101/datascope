import pandas as pd
import plotly.express as px
import streamlit as st

dataset = pd.read_csv("./population-data/world-population-forcast-2020-2050.csv")
# dataset = st.file_uploader("Upload a CSV dataset", type=["csv"])

st.write("<h1>Dataset visualization</h1>", unsafe_allow_html=True)
st.dataframe(dataset)  # or st.table (as static table)

fix = px.bar(
    dataset,
    x="Year",
    y="Population",
    color="Year",
    title="Population in the world from 2020 to 2050",
)
st.plotly_chart(fix)
