import streamlit as st
import pandas as pd
import numpy as np
@st.cache_data
def load_data(url):
    df = pd.read_csv(url)
    return df
df = load_data("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")
st.dataframe(df)
st.button("rerun")