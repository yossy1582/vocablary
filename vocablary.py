import numpy as np
import pandas as pd
import streamlit as st

import os, sys
 

answer_num = 10

check = False
pwd = os.getcwd()
st.title("VOCABLARIES CARD ")

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

mode = st.sidebar.radio('mode', ('sequential', 'random', 'reverse'))


english  = data['English']
japanese = data['Japanese']

st.write(english)

num=3
col1, col2, col3 = st.columns(3)

for n in range(num):

    with col1:
        st.write(english[n])
    with col2:
        st.text_input(" ")
    with col3:
        st.write(" ")


# col= st.columns(num)
# for n in range(answer_num):
#     for lst in list(range(0,num,1)):
#         if check:
#             with col[lst]:
#                 st.write(japanese[n])
#                 st.text_input(" ")
#         else:
#             with col[lst]:
#                 st.write(english[n])
#                 st.text_input(" ")
#                 st.write(" ")



check = st.button("check")

