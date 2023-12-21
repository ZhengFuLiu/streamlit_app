import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import datetime
import os
from dateutil.relativedelta import relativedelta

def render_sidebar():
    with st.sidebar:
        st.markdown('''提供各設備歷史電壓走勢圖，提早排除異常。''')

def main_content():
    st.title('電壓圖表')
    st.markdown("#")
    st.markdown(f"""
            <div style='background-color: #19D3F3; padding: 10px; border-radius: 5px;'>
                <p style='color: black; font-size: 20px; margin: 0;'>查詢條件</p>
            </div>
            """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        part_name = st.selectbox('堆高機編號',
                                    ('堆高機-001', '堆高機-002', '堆高機-003', '堆高機-004', '堆高機-C001', '堆高機-C002'),
                                    index=None
                                )
    with col2:
        start_time = st.date_input("開始日期", datetime.date.today())
    with col3:
        end_time = st.date_input("結束日期", datetime.date.today())

    col1_down, col2_down = st.columns(2)
    with col1_down:
        if ("C" in str(part_name)):
            department_options = st.selectbox('特徵',
                                                ('啟閉', '電池溫度1', '總電壓', '電池液位'),
                                                index=None
                                            )
        elif ("C" not in str(part_name)) & ("-" in str(part_name)):
            department_options = st.selectbox('特徵',
                                                ('啟閉', '總電壓', '電池液位', '電池電流', '總電壓差'),
                                                index=None
                                            )
        else:
            department_options = st.selectbox('特徵',
                                                (''),
                                                index=None
                                            )
            disabled = True
    with col2_down:
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
    
    return b, part_name, department_options, [pd.to_datetime(str(start_time)), pd.to_datetime(str(end_time)) + relativedelta(days=1) - relativedelta(seconds=1)]

def plot_present(part_name, department_options, date_range):
    #確定工作目錄
    folder_directory = os.path.abspath(os.getcwd())
    if part_name == None:
            st.error('請選擇堆高機', icon="🚨")
    else:
        item_name = part_name.split("-")[1]
        if department_options == None:
            st.error('請選擇特徵', icon="🚨")
        else:
            try:
                data = pd.read_csv(f"{folder_directory}/data/{item_name}.csv", encoding="Big5")
                data = data[[col for col in data.columns if not col.startswith('Unnamed')]]
                data["時間"] = pd.to_datetime(data["時間"])
                df = data[(data["時間"] >= date_range[0]) & (data["時間"] <= date_range[1])]
                if department_options == "總電壓":
                    fig = go.Figure()
                    fig.add_trace(go.Scatter(x = df["時間"], y = df["總電壓"], mode = "markers+lines", name = "總電壓", marker = dict(size = 4, color = "#00FE35"), line = dict(color='black', width=2)))
                    fig.add_trace(go.Scatter(x = df["時間"][df["總電壓"] > 60], y = df["總電壓"][df["總電壓"] > 60], mode = "markers", name = "超過標準", marker = dict(size = 8, color = "firebrick")))
                    fig.add_trace(go.Scatter(x = df["時間"][df["總電壓"] < 40], y = df["總電壓"][df["總電壓"] < 40], mode = "markers", name = "低於標準", marker = dict(size = 8, color = "royalblue")))
                    fig.add_hline(y=40, line_dash="dash", line_color="blue")
                    fig.add_hline(y=60, line_dash="dash", line_color="red")
                    fig.update_xaxes(range = [date_range[0], date_range[1]])
                    fig.update_layout(xaxis_title='時間',
                                    yaxis_title=department_options,
                                    autosize=False,
                                    width=2000,
                                    height=600)
                    
                    st.plotly_chart(fig, theme=None, use_container_width=True)
                else:
                    fig = go.Figure()
                    fig.add_trace(go.Scatter(x = df["時間"], y = df[department_options], mode = "markers+lines", name = department_options, marker = dict(size = 4, color = "#00FE35"), line = dict(color='black', width=2)))
                    fig.update_xaxes(range = [date_range[0], date_range[1]])
                    fig.update_layout(xaxis_title='時間',
                                    yaxis_title=department_options,
                                    autosize=False,
                                    width=2000,
                                    height=600)
                    
                    st.plotly_chart(fig, theme=None, use_container_width=True)
            except Exception as e:
                st.success('No items to display.', icon="✅")


if __name__ == "__main__":
    #網頁呈現資訊
    st.set_page_config(
        page_title="電壓圖表",
        page_icon="🚜",
        initial_sidebar_state="auto",
        menu_items={
            'About': "勤工設備保養系統"
        } 
    )
    #邊頁設計
    render_sidebar()
    #內容設計
    b, part_name, department_options, date_range = main_content()
    if b:
        plot_present(part_name, department_options, date_range)