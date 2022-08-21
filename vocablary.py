import numpy as np
import pandas as pd
import streamlit as st

import os, sys
 


pwd = os.getcwd()
st.title("VOCABLARIES CARD " + pwd)

data = pd.read_csv("/data/vocablaries.csv")
st.dataframe(data)

st.sidebar.title("MENU")

