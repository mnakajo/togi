from difflib import diff_bytes
from re import S
import pandas as pd
import streamlit as st
import pydeck as pdk
import plotly.express as px
import matplotlib.pyplot as plt

from email.mime import image
from PIL import Image

st.title('都議会議員調査ダッシュボード')
st.header('都議会議員調査：2018-2021')
st.subheader('津田塾大学中條研究室')

df_ts =pd.read_csv('/Users/mnakajo/workspace/lec_togi/csv_data/tsdata.csv')


show_df = st.checkbox('Show DataFrame')
if show_df == True:
    st.write(df_ts)


fig=px.scatter(df_ts,
                x='イデオロギー',
                y='知事評価',
                range_x=[0,11],
                range_y=[0,11],
                color='会派',
                animation_frame='調査年')

st.plotly_chart(fig)


st.text('出典：津田塾大学　東京都議会議員調査2018-2021（津田塾大学中條研究室）')