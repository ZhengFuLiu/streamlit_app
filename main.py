import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
from utils import page1, page2, page3

if 'authenticated' not in st.session_state:
    st.session_state['authenticated'] = False

with open('./config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

def check_authentication():
    if not st.session_state['authenticated']:
        st.warning('請先登入。')
        st.stop()

def login():
    #yaml資訊
    authenticator = stauth.Authenticate(
        config['credentials'],
        config['cookie']['name'],
        config['cookie']['key'],
        config['cookie']['expiry_days'],
        config['preauthorized']
    )
    #登入頁面
    name, authentication_status, username = authenticator.login('登入', 'main')
    if authentication_status:
        st.session_state['authenticated'] = True
        col1, col2 = st.columns(2)
        with col1:
            st.write(f'歡迎 *管理員*')
        with col2:
            m = st.markdown("""
            <style>
            div.stButton > button:first-child {
                box-shadow: 3px 4px 0px 0px #3e7327;
                background:linear-gradient(to bottom, #77b55a 5%, #72b352 100%);
                background-color:#77b55a;
                border-radius:18px;
                border:1px solid #4b8f29;
                display:inline-block;
                cursor:pointer;
                color:black;
                font-family:Arial;
                font-size:17px;
                padding:7px 25px;
                text-decoration:none;
                text-shadow:0px 1px 0px #5b8a3c;
            }
            div.stButton > button:hover {
                background:linear-gradient(to bottom, #72b352 5%, #77b55a 100%);
                background-color:#72b352;
            }
            div.stButton > button:active {
                background: none;
            }
            </style>""", unsafe_allow_html=True)

            b = st.button("Logout")
            if b:
                logout()
    elif authentication_status == False:
        st.error('帳號或密碼錯誤')
    elif authentication_status == None:
        st.warning('請輸入帳號密碼')

def logout():
    # 登出
    st.session_state['authenticated'] = False
    # 刪除快取
    if 'authentication_status' in st.session_state:
        st.session_state['authentication_status'] = None
    # 重整
    st.experimental_rerun()

def login_page():
    login()
    main_page()

def main_page():
    #主頁設定
    st.title('⚜設備保養系統')
    st.markdown('#')
    st.write(' -    **即時監控各設備使用情形**')
    st.write(' -    **圖表顯示，一眼把握狀況**')
    st.write(' -    **AI大數據分析，設備異常及時告警**')
    st.markdown('#')

def other1_page():
    check_authentication()  # 檢查是否登入
    #邊頁設計
    page1.render_sidebar()
    #內容設計
    page1.main_content()

def other2_page():
    check_authentication()  # 檢查是否登入
    #邊頁設計
    page2.render_sidebar()
    #上半區內容設計
    page2.main_content()
    #選取機台型號
    part_name = page2.select_part_name()
    #選取日期區間
    b, date_time_range = page2.date_and_time_range_selection()
    #判斷按鈕觸發並生成文本
    if b:
        page2.df_present(part_name, date_time_range)

def other3_page():
    check_authentication()  # 檢查是否登入
    #邊頁設計
    page3.render_sidebar()
    #內容設計
    b, part_name, department_options, date_range = page3.main_content()
    if b:
        page3.plot_present(part_name, department_options, date_range)

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

    #頁面導覽
    page = st.sidebar.radio("選擇頁面", ["登入", "設備監控", "歷史資料", "電壓圖表"])
    
    if page == "登入":
        login_page()
    elif page == "設備監控":
        other1_page()
    elif page == "歷史資料":
        other2_page()
    elif page == "電壓圖表":
        other3_page()