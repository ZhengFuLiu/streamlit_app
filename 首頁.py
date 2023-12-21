import streamlit as st
import streamlit_authenticator as stauth

def main_page():
    #主頁設定
    st.title('⚜設備保養系統')
    st.markdown('#')
    st.write(' -    **即時監控各設備使用情形**')
    st.write(' -    **圖表顯示，一眼把握狀況**')
    st.write(' -    **AI大數據分析，設備異常及時告警**')
    st.markdown('#')

if __name__ == "__main__":
    #網頁呈現資訊
    st.set_page_config(
        page_title="Axon",
        page_icon="🚜",
        initial_sidebar_state="auto",
        menu_items={
            'About': "勤工設備保養系統"
        } 
    )
    main_page()