import streamlit as st
from streamlit_lottie import st_lottie
import json
import requests

# Custom CSS to position and style the Lottie animation
st.markdown("""
    <style>
        .lottie-top-left {
            position: absolute;
            top: 30px;
            left: 30px;
            width: 300px; /* bigger size */
            height: 300px;
            z-index: 999;
        }
        .block-container {
            padding-top: 100px;
        }
    </style>
""", unsafe_allow_html=True)

# Load Lottie from file
def load_lottie_file(path: str):
    with open(path, "r") as file:
        return json.load(file)

# Load animations
lottie_top_left = load_lottie_file("lottie_anim1.json")
lottie_main = load_lottie_file("lottie_anim2.json")

# Render top-left animation (injected into a custom div)
lottie_html = f"""
<div class="lottie-top-left">
    {st_lottie(lottie_top_left, height=300, width=300, key="left")}
</div>
"""
st.components.v1.html(lottie_html, height=0)

# Main content
st.title("Main Content Area")
st_lottie(lottie_main, height=250, key="main")

