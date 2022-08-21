import numpy as np
import pandas as pd
import streamlit as st

 



st.title("VOCABLARIES CARD")

data = pd.read_csv("data/vocablaries.csv")
st.dataframe(data)

st.sidebar.title("MENU")

