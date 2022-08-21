import numpy as np
import pandas as pd
import streamlit as st

import os, sys
 


pwd = os.getcwd()
st.title("VOCABLARIES CARD " + pwd)

data = pd.read_csv("./data/vocablaries.csv", encoding='shift_jis')
# data = pd.read_csv("/app/vocablary/data/bocablaries.csv")
st.dataframe(data.head())

st.sidebar.title("MENU")

