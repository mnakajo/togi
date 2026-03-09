import pandas as pd
import streamlit as st
import pydeck as pdk
import plotly.express as px

st.title('都議会議員調査時系列')
st.header('2018-2025')
st.subheader('津田塾大学中條研究室')
st.markdown("<hr>",unsafe_allow_html=True)

df_ts =pd.read_csv("csv_data/tsdata8.csv")

df_ideo_counts = (
    df_ts.groupby(['調査年','イデオロギー'])
         .size()
         .reset_index(name='頻度')
)

fig2=px.bar(df_ideo_counts,
                x='イデオロギー',
                y="頻度",
                range_y=[0, df_ideo_counts['頻度'].max()+5] ,
                range_x=[-1,11],
                color='イデオロギー', 
                color_continuous_scale='RdBu' ,
                animation_frame='調査年')

fig2.update_layout(coloraxis_showscale=False)

st.markdown("#### イデオロギー")
st.write("異なる政治立場を表すとき、「保守」と「リベラル」、あるいは「右派」と「左派」などと表現することがあります。最も右派・保守的な立場を10、最も左派・リベラルな立場を0とした場合、あなたの政治的立場に最も近い数字をお答えください。")
st.plotly_chart(fig2, use_container_width=True)
st.caption('出典：津田塾大学　東京都議会議員調査2018-2025（津田塾大学中條研究室）')

df_gov_counts = (
    df_ts.groupby(['調査年','知事評価'])
         .size()
         .reset_index(name='頻度')
)

fig3=px.bar(df_gov_counts,
                x='知事評価',
                y="頻度",
                range_y=[0, df_gov_counts['頻度'].max()+5] ,
                range_x=[-1,11],
                color='知事評価', 
                color_continuous_scale="Greens",
                animation_frame='調査年')

fig3.update_layout(coloraxis_showscale=False)

st.markdown("#### 知事評価")
st.write("現在の東京都知事の仕事ぶりについて、0（全くやっていない）から10（とてもよくやっている）とすると、あなたの評価は何点でしょうか。")
st.plotly_chart(fig3, use_container_width=True)
st.caption('出典：津田塾大学　東京都議会議員調査2018-2025（津田塾大学中條研究室）')

st.markdown(
    "<hr><p style='text-align:center; color:gray; font-size:12px;'>© 2026 Miwa Nakajo. All rights reserved.</p>",
    unsafe_allow_html=True
)
