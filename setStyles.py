import streamlit as st
import base64

def set_styles(jpg_file):
    with open(jpg_file, "rb") as f:
        base64_img = base64.b64encode(f.read()).decode()
    css = f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{base64_img}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}

    .stButton > button:disabled {{
        background: rgb(19, 23, 32) !important;
        color: #666666 !important;
        cursor: not-allowed;
    }}

    .stButton > button {{
        background: rgb(19, 23, 32);
        color: white;
    }}
    </style>
    """
    
    st.markdown(css, unsafe_allow_html=True)
