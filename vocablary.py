import numpy as np
import pandas as pd
import streamlit as st

import os, sys
 


pwd = os.getcwd()
st.title("VOCABLARIES CARD " + pwd)

data = pd.read_csv("./data/vocablaries.csv", encoding='shift_jis', index_col=None)
# st.dataframe(data.head())

unit = data['UNIT'].values
st.write(unit)


st.sidebar.title("MENU")

