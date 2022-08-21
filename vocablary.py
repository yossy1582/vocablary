import numpy as np
import pandas as pd
import streamlit as st

import os, sys
 


pwd = os.getcwd()
st.title("VOCABLARIES CARD " + pwd)

data = pd.read_csv("./data/vocablaries.csv", encoding='shift_jis')
# st.dataframe(data.head())

unit = np.array(data['UNIT'])
st.write(unit)


st.sidebar.title("MENU")

