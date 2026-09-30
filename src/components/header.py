import streamlit as st

def header_home():
    logo_path ="https://i.ibb.co/Fky7tq2B/Chat-GPT-Image-Sep-28-2026-12-09-18-PM.png"
    
    st.markdown(f"""

         <div style='display:flex; flex-direction:column; align-item: center; justify-content:center; margin-bottom:30px; margin-top:30px;'>

         <img src='{logo_path}' style='height:100px;'>
         <h1 style='text-align: center; color: #E0E3FF'> Snap<br>Class</h1>

         </div>

               """,
               unsafe_allow_html=True

    )