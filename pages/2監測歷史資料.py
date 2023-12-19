import streamlit as st
import datetime

def render_sidebar():
    with st.sidebar:
        st.markdown('''選取時間區間，一鍵輸出歷史報表。''')

def render_title():
    st.title('監測歷史資料')
    st.markdown("#")
    st.markdown(f"""
            <div style='background-color: #19D3F3; padding: 10px; border-radius: 5px;'>
                <p style='color: black; font-size: 20px; margin: 0;'>查詢頁面</p>
            </div>
            """, unsafe_allow_html=True)

def select_part_name():
    return st.selectbox('部品名稱',
                        ('堆高機001', '堆高機002', '堆高機003', '堆高機004', '堆高機C001', '堆高機C002'),
                        index=None)

def date_and_time_range_selection():
    col1, col2 = st.columns(2)
    with col1:
        output = st.radio(
                "日期類型 👇",
                ["日期區間", "預先定義的日期"],
                horizontal=True,
            )
        
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
            position:relative;
            top:1px;
        }
        </style>""", unsafe_allow_html=True)

        b = st.button("🔍查詢")
        if b & (part_name != None):
            st.write("No items to display")
        elif b & (part_name == None):
            st.error('請選擇堆高機', icon="🚨")
        else:
            st.write("")

    with col2:
        if output == "日期區間":
            start_date = st.date_input("開始日期", datetime.date.today())
            end_date = st.date_input("結束日期", datetime.date.today())
            start_time = st.time_input("開始時間", datetime.time(8, 0))
            end_time = st.time_input("結束時間", datetime.time(16, 45))
            return (start_date, start_time), (end_date, end_time)
        else:
            return st.selectbox('日期區間',
                                ('這個月', '上個月', '上一季', '上半年'),
                                index=None), None

# Main code execution
render_sidebar()
render_title()
part_name = select_part_name()
date_time_range = date_and_time_range_selection()