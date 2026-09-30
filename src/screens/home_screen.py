import streamlit as st
from src.components.header import header_home
from src.components.footer import footer_home
from src.ui.base_layout import style_base_layout, style_background_home


def home_screen():
    header_home()
    style_base_layout()
   
    style_background_home()
    
    
   

    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.header("I'am Student")
        st.image("https://res.cloudinary.com/mq5cwwm5/image/upload/v1790580545/ChatGPT_Image_Sep_28_2026_12_56_12_PM.png", width=120)
        if st.button('Student Portal', type="primary", icon=':material/arrow_outward:', icon_position="right"):
            st.session_state['login_type']='student'
            st.rerun()

    with col2:
        st.header("I'am Teacher")
        st.image("https://res.cloudinary.com/mq5cwwm5/image/upload/v1790580829/ChatGPT_Image_Sep_28_2026_01_03_17_PM.png", width=120)
        if st.button('Teacher Portal', type="primary", icon=':material/arrow_outward:', icon_position="right"):
            st.session_state['login_type']='teacher'
            st.rerun()

    footer_home()
