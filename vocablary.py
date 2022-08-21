import numpy as np
import pandas as pd
import streamlit as st

import os, sys
 


pwd = os.getcwd()
st.title("VOCABLARIES CARD " + pwd)

data = pd.read_csv("data/bocablaries.csv")
# data = pd.read_csv("/app/vocablary/data/bocablaries.csv")
st.dataframe(data)

st.sidebar.title("MENU")

