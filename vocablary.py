import numpy as np
import pandas as pd
import streamlit as st

import os, sys
 


pwd = os.getcwd()
st.title("VOCABLARIES CARD " + pwd)

data = pd.read_csv("./data/vocablaries.csv", encoding='shift_jis', index_col=None)
# st.dataframe(data.head())

unit_list = data['UNIT'].unique()
part_list = data['Part'].unique()
# st.write(unit)
level_list = (0,1,2,3,4,5)


st.sidebar.title("MENU")
unit = st.sidebar.selectbox("UNIT", unit_list)
part = st.sidebar.selectbox("Part", part_list)
level = st.sidebar.multiselect("Level", level_list)
