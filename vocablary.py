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
# part_list = data['Part'].unique()
# st.write(unit)
level_list = (0,1,2,3,4,5)



#############################################
st.sidebar.title("MENU")
unit = st.sidebar.selectbox("UNIT", unit_list)
part_list = data[data['UNIT'] == unit].unique()
st.write(part_list)

part = st.sidebar.selectbox("Part", part_list)
level = st.sidebar.multiselect("Level", level_list)

mode = st.sidebar.radio('mode', ('sequential', 'random', 'reverse'))
#############################################




question = data[(data['UNIT'] == unit) & (data['Part'] == part)]
english  = question['English']
japanese = question['Japanese']

st.write(english)

num=3

if check != 1:
    for n in range(answer_num):
        if(n < english.shape[0]):
            col1, col2, col3 = st.columns(3)

            with col1:
                st.text_input('japanese ' + str(n), japanese[n])
            with col2:
                j = st.text_input('eglish ' + str(n))
            with col3:
                st.write("eee")



check = st.button("check")

