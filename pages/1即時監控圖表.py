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

def main_content():
    st.title("即時監測圖表")
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

    cb1, cb2, cb3, cb4 = st.columns(4)
    on = cb1.checkbox('運行中', value=True)
    stop = cb2.checkbox('停止', value=True)
    off = cb3.checkbox('關機', value=True)
    ng = cb4.checkbox('異常', value=True)

    st.markdown("#")
    st.markdown(f"""
        <div style='background-color: #19D3F3; padding: 10px; border-radius: 5px;'>
            <p style='color: black; font-size: 20px; margin: 0;'>{option}{''.join(department_options)}</p>
        </div>
        """, unsafe_allow_html=True)

    if (f"{option}{''.join(department_options)}" == "總公司業務部") & (on):
        card1, card2 = st.columns(2, gap="small")
        with card1:
            st.markdown("""
                <div style='background-color: #34A853; padding: 10px; border-radius: 5px 5px 0 0; text-align: center;'>
                    <p style='color: white; font-size: 32px; margin: 0;'>堆高機003</p>
                </div>
                """, unsafe_allow_html=True)

            subrule1_c1, subrule2_c1 = st.columns([1, 1], gap="small")
            with subrule1_c1:
                st.markdown("""
                    <div style='background-color: #34A853; padding: 10px; margin-right: -10px; text-align: center;'>
                        <p style='color: white; font-size: 14px; margin: 0;'>使用時數:--</p>
                    </div>
                    """, unsafe_allow_html=True)
            with subrule2_c1:
                st.markdown("""
                    <div style='background-color: #34A853; padding: 10px; margin-left: -10px; text-align: center;'>
                        <p style='color: white; font-size: 14px; margin: 0;'>稼動率:--%</p>
                    </div>
                    """, unsafe_allow_html=True)
            
            mat1_c1, mat2_c1 = st.columns(2)
            with mat1_c1:
                st.markdown("""
                    <div style='background-color: white; padding: 10px; border-radius: 5px;'>
                        <p style='color: #34A853; font-size: 20px; margin: 0;'>31.60 °C</p>
                        <p style='color: black; font-size: 16px; margin: 0;'>電池溫度</p>
                    </div>
                    """, unsafe_allow_html=True)
            with mat2_c1:
                st.markdown("""
                    <div style='background-color: white; padding: 10px; border-radius: 5px;'>
                        <p style='color: #34A853; font-size: 20px; margin: 0;'>49.09 V</p>
                        <p style='color: black; font-size: 16px; margin: 0;'>總電壓</p>
                    </div>
                    """, unsafe_allow_html=True)
            st.markdown("""
                    <div style='background-color: white; padding: 10px; border-radius: 5px;'>
                        <p style='color: #34A853; font-size: 20px; margin: 0;'>正常 (狀態)</p>
                        <p style='color: black; font-size: 16px; margin: 0;'>電池液位</p>
                    </div>
                    """, unsafe_allow_html=True)

        with card2:
            st.markdown("""
                <div style='background-color: #34A853; padding: 10px; border-radius: 5px 5px 0 0; text-align: center;'>
                    <p style='color: white; font-size: 32px; margin: 0;'>堆高機004</p>
                </div>
                """, unsafe_allow_html=True)

            subrule1_c2, subrule2_c2 = st.columns([1, 1], gap="small")
            with subrule1_c2:
                st.markdown("""
                    <div style='background-color: #34A853; padding: 10px; margin-right: -10px; text-align: center;'>
                        <p style='color: white; font-size: 14px; margin: 0;'>使用時數:--</p>
                    </div>
                    """, unsafe_allow_html=True)
            with subrule2_c2:
                st.markdown("""
                    <div style='background-color: #34A853; padding: 10px; margin-left: -10px; text-align: center;'>
                        <p style='color: white; font-size: 14px; margin: 0;'>稼動率:--%</p>
                    </div>
                    """, unsafe_allow_html=True)
                
            mat1_c2, mat2_c2 = st.columns(2)
            with mat1_c2:
                st.markdown("""
                    <div style='background-color: white; padding: 10px; border-radius: 5px;'>
                        <p style='color: #34A853; font-size: 20px; margin: 0;'>35.40 °C</p>
                        <p style='color: black; font-size: 16px; margin: 0;'>電池溫度</p>
                    </div>
                    """, unsafe_allow_html=True)
            with mat2_c2:
                st.markdown("""
                    <div style='background-color: white; padding: 10px; border-radius: 5px;'>
                        <p style='color: #34A853; font-size: 20px; margin: 0;'>45.07 V</p>
                        <p style='color: black; font-size: 16px; margin: 0;'>總電壓</p>
                    </div>
                    """, unsafe_allow_html=True)
            st.markdown("""
                    <div style='background-color: white; padding: 10px; border-radius: 5px;'>
                        <p style='color: #34A853; font-size: 20px; margin: 0;'>正常 (狀態)</p>
                        <p style='color: black; font-size: 16px; margin: 0;'>電池液位</p>
                    </div>
                    """, unsafe_allow_html=True)
            
    if (f"{option}{''.join(department_options)}" == "客戶服務客戶100"):
        if on & off:
            card1, card2 = st.columns(2, gap="small")
            with card1:
                st.markdown("""
                    <div style='background-color: #7F7F7F; padding: 10px; border-radius: 5px 5px 0 0; text-align: center;'>
                        <p style='color: white; font-size: 32px; margin: 0;'>堆高機C001</p>
                    </div>
                    """, unsafe_allow_html=True)

                subrule1_c1, subrule2_c1 = st.columns([1, 1], gap="small")
                with subrule1_c1:
                    st.markdown("""
                        <div style='background-color: #7F7F7F; padding: 10px; margin-right: -10px; text-align: center;'>
                            <p style='color: white; font-size: 14px; margin: 0;'>使用時數:--</p>
                        </div>
                        """, unsafe_allow_html=True)
                with subrule2_c1:
                    st.markdown("""
                        <div style='background-color: #7F7F7F; padding: 10px; margin-left: -10px; text-align: center;'>
                            <p style='color: white; font-size: 14px; margin: 0;'>稼動率:--%</p>
                        </div>
                        """, unsafe_allow_html=True)
                
                mat1_c1, mat2_c1 = st.columns(2)
                with mat1_c1:
                    st.markdown("""
                        <div style='background-color: white; padding: 10px; border-radius: 5px;'>
                            <p style='color: #7F7F7F; font-size: 20px; margin: 0;'>30.50 °C</p>
                            <p style='color: black; font-size: 16px; margin: 0;'>電池溫度</p>
                        </div>
                        """, unsafe_allow_html=True)
                with mat2_c1:
                    st.markdown("""
                        <div style='background-color: white; padding: 10px; border-radius: 5px;'>
                            <p style='color: #7F7F7F; font-size: 20px; margin: 0;'>49.52 V</p>
                            <p style='color: black; font-size: 16px; margin: 0;'>總電壓</p>
                        </div>
                        """, unsafe_allow_html=True)
                st.markdown("""
                        <div style='background-color: white; padding: 10px; border-radius: 5px;'>
                            <p style='color: #7F7F7F; font-size: 20px; margin: 0;'>正常 (狀態)</p>
                            <p style='color: black; font-size: 16px; margin: 0;'>電池液位</p>
                        </div>
                        """, unsafe_allow_html=True)

            with card2:
                st.markdown("""
                    <div style='background-color: #34A853; padding: 10px; border-radius: 5px 5px 0 0; text-align: center;'>
                        <p style='color: white; font-size: 32px; margin: 0;'>堆高機C002</p>
                    </div>
                    """, unsafe_allow_html=True)

                subrule1_c2, subrule2_c2 = st.columns([1, 1], gap="small")
                with subrule1_c2:
                    st.markdown("""
                        <div style='background-color: #34A853; padding: 10px; margin-right: -10px; text-align: center;'>
                            <p style='color: white; font-size: 14px; margin: 0;'>使用時數:--</p>
                        </div>
                        """, unsafe_allow_html=True)
                with subrule2_c2:
                    st.markdown("""
                        <div style='background-color: #34A853; padding: 10px; margin-left: -10px; text-align: center;'>
                            <p style='color: white; font-size: 14px; margin: 0;'>稼動率:--%</p>
                        </div>
                        """, unsafe_allow_html=True)
                    
                mat1_c2, mat2_c2 = st.columns(2)
                with mat1_c2:
                    st.markdown("""
                        <div style='background-color: white; padding: 10px; border-radius: 5px;'>
                            <p style='color: #34A853; font-size: 20px; margin: 0;'>35.40 °C</p>
                            <p style='color: black; font-size: 16px; margin: 0;'>電池溫度</p>
                        </div>
                        """, unsafe_allow_html=True)
                with mat2_c2:
                    st.markdown("""
                        <div style='background-color: white; padding: 10px; border-radius: 5px;'>
                            <p style='color: #34A853; font-size: 20px; margin: 0;'>45.07 V</p>
                            <p style='color: black; font-size: 16px; margin: 0;'>總電壓</p>
                        </div>
                        """, unsafe_allow_html=True)
                st.markdown("""
                        <div style='background-color: white; padding: 10px; border-radius: 5px;'>
                            <p style='color: #34A853; font-size: 20px; margin: 0;'>正常 (狀態)</p>
                            <p style='color: black; font-size: 16px; margin: 0;'>電池液位</p>
                        </div>
                        """, unsafe_allow_html=True)
        elif on:
            st.markdown("""
                <div style='background-color: #34A853; padding: 10px; border-radius: 5px 5px 0 0; text-align: center;'>
                    <p style='color: white; font-size: 32px; margin: 0;'>堆高機C002</p>
                </div>
                """, unsafe_allow_html=True)

            subrule1_c2, subrule2_c2 = st.columns([1, 1], gap="small")
            with subrule1_c2:
                st.markdown("""
                    <div style='background-color: #34A853; padding: 10px; margin-right: -10px; text-align: center;'>
                        <p style='color: white; font-size: 14px; margin: 0;'>使用時數:--</p>
                    </div>
                    """, unsafe_allow_html=True)
            with subrule2_c2:
                st.markdown("""
                    <div style='background-color: #34A853; padding: 10px; margin-left: -10px; text-align: center;'>
                        <p style='color: white; font-size: 14px; margin: 0;'>稼動率:--%</p>
                    </div>
                    """, unsafe_allow_html=True)
                
            mat1_c2, mat2_c2 = st.columns(2)
            with mat1_c2:
                st.markdown("""
                    <div style='background-color: white; padding: 10px; border-radius: 5px;'>
                        <p style='color: #34A853; font-size: 20px; margin: 0;'>35.40 °C</p>
                        <p style='color: black; font-size: 16px; margin: 0;'>電池溫度</p>
                    </div>
                    """, unsafe_allow_html=True)
            with mat2_c2:
                st.markdown("""
                    <div style='background-color: white; padding: 10px; border-radius: 5px;'>
                        <p style='color: #34A853; font-size: 20px; margin: 0;'>45.07 V</p>
                        <p style='color: black; font-size: 16px; margin: 0;'>總電壓</p>
                    </div>
                    """, unsafe_allow_html=True)
            st.markdown("""
                    <div style='background-color: white; padding: 10px; border-radius: 5px;'>
                        <p style='color: #34A853; font-size: 20px; margin: 0;'>正常 (狀態)</p>
                        <p style='color: black; font-size: 16px; margin: 0;'>電池液位</p>
                    </div>
                    """, unsafe_allow_html=True)
        elif off: 
            st.markdown("""
                <div style='background-color: #7F7F7F; padding: 10px; border-radius: 5px 5px 0 0; text-align: center;'>
                    <p style='color: white; font-size: 32px; margin: 0;'>堆高機C001</p>
                </div>
                """, unsafe_allow_html=True)

            subrule1_c1, subrule2_c1 = st.columns([1, 1], gap="small")
            with subrule1_c1:
                st.markdown("""
                    <div style='background-color: #7F7F7F; padding: 10px; margin-right: -10px; text-align: center;'>
                        <p style='color: white; font-size: 14px; margin: 0;'>使用時數:--</p>
                    </div>
                    """, unsafe_allow_html=True)
            with subrule2_c1:
                st.markdown("""
                    <div style='background-color: #7F7F7F; padding: 10px; margin-left: -10px; text-align: center;'>
                        <p style='color: white; font-size: 14px; margin: 0;'>稼動率:--%</p>
                    </div>
                    """, unsafe_allow_html=True)
            
            mat1_c1, mat2_c1 = st.columns(2)
            with mat1_c1:
                st.markdown("""
                    <div style='background-color: white; padding: 10px; border-radius: 5px;'>
                        <p style='color: #7F7F7F; font-size: 20px; margin: 0;'>30.50 °C</p>
                        <p style='color: black; font-size: 16px; margin: 0;'>電池溫度</p>
                    </div>
                    """, unsafe_allow_html=True)
            with mat2_c1:
                st.markdown("""
                    <div style='background-color: white; padding: 10px; border-radius: 5px;'>
                        <p style='color: #7F7F7F; font-size: 20px; margin: 0;'>49.52 V</p>
                        <p style='color: black; font-size: 16px; margin: 0;'>總電壓</p>
                    </div>
                    """, unsafe_allow_html=True)
            st.markdown("""
                    <div style='background-color: white; padding: 10px; border-radius: 5px;'>
                        <p style='color: #7F7F7F; font-size: 20px; margin: 0;'>正常 (狀態)</p>
                        <p style='color: black; font-size: 16px; margin: 0;'>電池液位</p>
                    </div>
                    """, unsafe_allow_html=True)     
            
main_content()