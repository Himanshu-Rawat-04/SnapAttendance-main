import streamlit as st

def header_home():
    logo_path ="https://res.cloudinary.com/mq5cwwm5/image/upload/v1791528987/Minimalist_Graduate_App_Icon.png"
    
    st.markdown(f"""

         <div style='display:flex; flex-direction:column; align-item: center; justify-content:center; margin-bottom:30px; margin-top:30px;'>

         <img src='{logo_path}' style='height:100px;'>
         <h1 style='text-align: center; color: #E0E3FF'> Snap<br>Attendance</h1>

         </div>

               """,
               unsafe_allow_html=True

    )


def header_dashboard():
    logo_path ="https://res.cloudinary.com/mq5cwwm5/image/upload/v1791528987/Minimalist_Graduate_App_Icon.png"
    
    st.markdown(f"""

         <div style='display:flex; align-item: center; justify-content:center; gap:10px;'>

         <img src='{logo_path}' style='height:85px;'>
         <h2 style='text-align: left; color: #5865F2'> Snap<br>Class </h2>

         </div>

               """,
               unsafe_allow_html=True

    )