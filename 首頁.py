import streamlit as st
import datetime

st.set_page_config(
    page_title="LeekLab",
    page_icon="🪙",
    initial_sidebar_state="expanded" 
)

st.markdown('# ⚜設備保養系統')
st.markdown('##')
st.write(' -    **即時監控各設備使用情形**')
st.write(' -    **圖表顯示，一眼把握狀況**')
st.write(' -    **AI大數據分析，設備異常及時告警**')
st.markdown('##')


# d = st.date_input("日期區間", datetime.date(2023, 9, 1))
# t = st.time_input("時間區間", datetime.time(8, 00))

# st.write('選取時間', d, t)