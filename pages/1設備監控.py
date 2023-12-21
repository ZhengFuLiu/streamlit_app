import streamlit as st
import pandas as pd

def create_data_block(title, value, background_color):
    """創建一個數據展示塊。"""
    return f"""
        <div style='background-color: {background_color}; padding: 10px; border-radius: 5px; text-align: center;'>
            <p style='color: black; font-size: 32px; margin: 0;'>{title}</p>
            <p style='color: black; font-size: 40px; margin: 0;'>{value}</p>
        </div>
        """

def render_sidebar():
    
    with st.sidebar:
        st.markdown('''即時反映目前運作狀況，透過設立搜索條件，迅速掌握設備是否異常。''')

def main_content():
    st.title("設備監控")
    st.markdown("#")

    # Data blocks
    t1, t2, t3, t4, t5 = st.columns(5)
    t1.markdown(create_data_block("總數", "4", "#636EFA"), unsafe_allow_html=True)
    t2.markdown(create_data_block("運行中", "2", "#34A853"), unsafe_allow_html=True)
    t3.markdown(create_data_block("停止", "0", "#FECB52"), unsafe_allow_html=True)
    t4.markdown(create_data_block("關機", "2", "#7F7F7F"), unsafe_allow_html=True)
    t5.markdown(create_data_block("異常", "0", "#EF553B"), unsafe_allow_html=True)

    # Main interactive components
    st.markdown("#")
    st.markdown(f"""
        <div style='background-color: #19D3F3; padding: 10px; border-radius: 5px;'>
            <p style='color: black; font-size: 20px; margin: 0;'>查詢條件</p>
        </div>
        """, unsafe_allow_html=True)
    col1, col2 = st.columns(2)

    with col1:
        option = st.selectbox('工廠', ('總公司', '客戶服務'), index=None)

    if option == "總公司":
        department_options = ('業務部',)
    elif option == "客戶服務":
        department_options = ("客戶100",)
    else:
        department_options = ("",)
        disabled = True

    # 顯示部門選項
    with col2:
        if 'disabled' in locals():  # 檢查是否需要禁用選項
            suboption = st.selectbox("部門", department_options, disabled=True)
        else:
            suboption = st.selectbox("部門", department_options)

    # 創建一個用於顯示卡片的函數
    def create_card(title, temp, voltage, status, color):
        return f"""
        <div style='background-color: {color}; padding: 10px; border-radius: 5px 5px 0 0; text-align: center;'>
            <p style='color: white; font-size: 32px; margin: 0;'>{title}</p>
        </div>
        <div style='background-color: white; padding: 10px; border-radius: 5px;'>
            <p style='color: {color}; font-size: 20px; margin: 0;'>{temp} °C</p>
            <p style='color: black; font-size: 16px; margin: 0;'>電池溫度</p>
            <p style='color: {color}; font-size: 20px; margin: 0;'>{voltage} V</p>
            <p style='color: black; font-size: 16px; margin: 0;'>總電壓</p>
            <p style='color: {color}; font-size: 20px; margin: 0;'>{status} (狀態)</p>
            <p style='color: black; font-size: 16px; margin: 0;'>電池液位</p>
        </div>
        """

    cb1, cb2, cb3, cb4 = st.columns(4)
    on = cb1.checkbox('運行中', value=True)
    stop = cb2.checkbox('停止', value=True)
    off = cb3.checkbox('關機', value=True)
    ng = cb4.checkbox('異常', value=True)

    department = f"{option}-{''.join(department_options)}"

    st.markdown("#")
    if department == "總公司-業務部":
        st.markdown(f"""
        <div style='background-color: #19D3F3; padding: 10px; border-radius: 5px;'>
            <p style='color: black; font-size: 20px; margin: 0;'>{department}</p>
        </div>
        """, unsafe_allow_html=True)

        if on:
            card1, card2 = st.columns(2, gap="small")
            with card1:
                st.markdown(create_card("堆高機003", "31.60", "49.09", "正常", "#34A853"), unsafe_allow_html=True)
            with card2:
                st.markdown(create_card("堆高機004", "35.40", "45.07", "正常", "#34A853"), unsafe_allow_html=True)

    if department == "客戶服務-客戶100":
        st.markdown(f"""
        <div style='background-color: #19D3F3; padding: 10px; border-radius: 5px;'>
            <p style='color: black; font-size: 20px; margin: 0;'>{department}</p>
        </div>
        """, unsafe_allow_html=True)

        if on & off:
            card1, card2 = st.columns(2, gap="small")
            with card1:
                st.markdown(create_card("堆高機C001", "30.50", "49.52", "正常", "#7F7F7F"), unsafe_allow_html=True)
            with card2:
                st.markdown(create_card("堆高機C002", "35.40", "45.07", "正常", "#34A853"), unsafe_allow_html=True)
        
        elif on:
            card1, card2 = st.columns(2, gap="small")
            with card1:
                st.markdown(create_card("堆高機C002", "35.40", "45.07", "正常", "#34A853"), unsafe_allow_html=True)
        elif off:
            card1, card2 = st.columns(2, gap="small")
            with card1:
                st.markdown(create_card("堆高機C001", "30.50", "49.52", "正常", "#7F7F7F"), unsafe_allow_html=True)

    if f"{option}{''.join(department_options)}" == "None":
        st.markdown(f"""
        <div style='background-color: #19D3F3; padding: 10px; border-radius: 5px;'>
            <p style='color: black; font-size: 20px; margin: 0;'>總公司-業務部</p>
        </div>
        """, unsafe_allow_html=True)
        if on & off:
            card1, card2 = st.columns(2, gap="small")
            with card1:
                st.markdown(create_card("堆高機003", "31.60", "49.09", "正常", "#34A853"), unsafe_allow_html=True)
            with card2:
                st.markdown(create_card("堆高機004", "35.40", "45.07", "正常", "#34A853"), unsafe_allow_html=True)
            st.markdown(f"""
            <div style='background-color: #19D3F3; padding: 10px; border-radius: 5px;'>
                <p style='color: black; font-size: 20px; margin: 0;'>客戶服務-客戶100</p>
            </div>
            """, unsafe_allow_html=True)
            card1, card2 = st.columns(2, gap="small")
            with card1:
                st.markdown(create_card("堆高機C001", "30.50", "49.52", "正常", "#7F7F7F"), unsafe_allow_html=True)
            with card2:
                st.markdown(create_card("堆高機C002", "35.40", "45.07", "正常", "#34A853"), unsafe_allow_html=True)
        elif on:
            card1, card2 = st.columns(2, gap="small")
            with card1:
                st.markdown(create_card("堆高機003", "31.60", "49.09", "正常", "#34A853"), unsafe_allow_html=True)
            with card2:
                st.markdown(create_card("堆高機004", "35.40", "45.07", "正常", "#34A853"), unsafe_allow_html=True)
            st.markdown(f"""
            <div style='background-color: #19D3F3; padding: 10px; border-radius: 5px;'>
                <p style='color: black; font-size: 20px; margin: 0;'>客戶服務-客戶100</p>
            </div>
            """, unsafe_allow_html=True)
            card1, card2 = st.columns(2, gap="small")
            with card1:
                st.markdown(create_card("堆高機C002", "35.40", "45.07", "正常", "#34A853"), unsafe_allow_html=True)
        elif off:
            st.markdown("#")
            st.markdown(f"""
            <div style='background-color: #19D3F3; padding: 10px; border-radius: 5px;'>
                <p style='color: black; font-size: 20px; margin: 0;'>客戶服務-客戶100</p>
            </div>
            """, unsafe_allow_html=True)
            card1, card2 = st.columns(2, gap="small")
            with card1:
                st.markdown(create_card("堆高機C001", "30.50", "49.52", "正常", "#7F7F7F"), unsafe_allow_html=True)

if __name__ == "__main__":
    #網頁呈現資訊
    st.set_page_config(
        page_title="設備監控",
        page_icon="🚜",
        initial_sidebar_state="auto",
        menu_items={
            'About': "勤工設備保養系統"
        } 
    )
    #邊頁設計
    render_sidebar()
    #內容設計
    main_content()