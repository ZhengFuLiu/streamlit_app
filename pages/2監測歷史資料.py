import streamlit as st
import pandas as pd
import datetime
from dateutil.relativedelta import relativedelta
import os

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
                        ('堆高機-001', '堆高機-002', '堆高機-003', '堆高機-004', '堆高機-C001', '堆高機-C002'),
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
            background: none;
        }
        </style>""", unsafe_allow_html=True)

        b = st.button("🔍查詢")
    with col2:
        if output == "日期區間":
            time_col1, time_col2 = st.columns(2)
            start_date = time_col1.date_input("開始日期", datetime.date.today())
            end_date = time_col1.date_input("結束日期", datetime.date.today())
            start_time = time_col2.time_input("開始時間", datetime.time(8, 0))
            end_time = time_col2.time_input("結束時間", datetime.time(16, 45))
            return b, [pd.to_datetime(str(start_date) + " " + str(start_time)), pd.to_datetime(str(end_date) + " " + str(end_time))]
        else:
            select_output = st.selectbox('日期區間', ('這個月', '上個月', '上一季', '上半年'), index=None)
            return b, select_output
        
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('Big5')

# Main code execution
folder_directory = os.path.abspath(os.getcwd())
render_sidebar()
render_title()
part_name = select_part_name()
b, date_time_range = date_and_time_range_selection()
if b:
    if part_name == None:
        st.error('請選擇堆高機', icon="🚨")
    else:
        item_name = part_name.split("-")[1]
        try:
            df = pd.read_csv(f"{folder_directory}/data/{item_name}.csv", encoding="Big5")
            data = df[[col for col in df.columns if not col.startswith('Unnamed')]]
            data["時間"] = pd.to_datetime(data["時間"])
            if len(date_time_range) == 2:
                subdf = data[(data["時間"] >= date_time_range[0]) & (data["時間"] <= date_time_range[1])]
                if len(subdf) > 0:
                    st.dataframe(subdf, use_container_width = True)
                    csv = convert_df(subdf)
                    col1, col2, col3, col4, col5 = st.columns(5)
                    with col5:
                        st.download_button(
                            label="📄 :blue[輸出報表]",
                            data=csv,
                            file_name=f'{part_name.replace("-", "")}({date_time_range[0].strftime("%Y%m%d")}_{date_time_range[1].strftime("%Y%m%d")}).csv',
                            mime='text/csv',
                        )
                else:
                    st.success('No items to display.', icon="✅")
            elif date_time_range == "這個月":
                start = pd.Timestamp(datetime.datetime.now().year, datetime.datetime.now().month, 1)
                end = pd.to_datetime(datetime.datetime.now())
                subdf = data[(data["時間"] >= start) & (data["時間"] <= end)]
                if len(subdf) > 0:
                    st.dataframe(subdf, use_container_width = True)
                    csv = convert_df(subdf)
                    col1, col2, col3, col4, col5 = st.columns(5)
                    with col5:
                        st.download_button(
                            label="📄 :blue[輸出報表]",
                            data=csv,
                            file_name=f'{part_name.replace("-", "")}({date_time_range}).csv',
                            mime='text/csv',
                        )
                else:
                    st.success('No items to display.', icon="✅")
            elif date_time_range == "上個月":
                start = pd.Timestamp(datetime.datetime.now().year, datetime.datetime.now().month - 1, 1)
                end = pd.Timestamp(datetime.datetime.now().year, datetime.datetime.now().month, 1) - relativedelta(seconds=1)
                subdf = data[(data["時間"] >= start) & (data["時間"] <= end)]
                if len(subdf) > 0:
                    st.dataframe(subdf, use_container_width = True)
                    csv = convert_df(subdf)
                    col1, col2, col3, col4, col5 = st.columns(5)
                    with col5:
                        st.download_button(
                            label="📄 :blue[輸出報表]",
                            data=csv,
                            file_name=f'{part_name.replace("-", "")}({date_time_range}).csv',
                            mime='text/csv',
                        )
                else:
                    st.success('No items to display.', icon="✅")
            elif date_time_range == "上一季":
                now = datetime.datetime.now()
                current_quarter_start = datetime.datetime(now.year, 3 * ((now.month - 1) // 3) + 1, 1)
                last_quarter_start = current_quarter_start - relativedelta(months=3)
                last_quarter_end = current_quarter_start - relativedelta(days=1)
                subdf = data[(data["時間"] >= last_quarter_start) & (data["時間"] <= last_quarter_end)]
                if len(subdf) > 0:
                    st.dataframe(subdf, use_container_width = True)
                    csv = convert_df(subdf)
                    col1, col2, col3, col4, col5 = st.columns(5)
                    with col5:
                        st.download_button(
                            label="📄 :blue[輸出報表]",
                            data=csv,
                            file_name=f'{part_name.replace("-", "")}({date_time_range}).csv',
                            mime='text/csv',
                        )
                else:
                    st.success('No items to display.', icon="✅")
            elif date_time_range == "上半年":
                first_half_start = datetime.date(datetime.datetime.now().year, 1, 1)
                first_half_end = datetime.date(datetime.datetime.now().year, 6, 30)
                subdf = data[(data["時間"] >= first_half_start) & (data["時間"] <= first_half_end)]
                if len(subdf) > 0:
                    st.dataframe(subdf, use_container_width = True)
                    csv = convert_df(subdf)
                    col1, col2, col3, col4, col5 = st.columns(5)
                    with col5:
                        st.download_button(
                            label="📄 :blue[輸出報表]",
                            data=csv,
                            file_name=f'{part_name.replace("-", "")}({date_time_range}).csv',
                            mime='text/csv',
                        )
                else:
                    st.success('No items to display.', icon="✅")
        except Exception as e:
            st.success('No items to display.', icon="✅")
