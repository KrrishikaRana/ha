import streamlit as st
st.markdown("""
    <style>
    .stApp {
        background-color: black;
        color: white;
    }
    
    iframe {
        background-color: transparent !important;
    }
    </style>
""", unsafe_allow_html=True)
from streamlit_lottie import st_lottie
import json

# Function to load the animation JSON
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

# Load the mood animation
lottie_mood = load_lottiefile("jj.json")
st.markdown("""
    <style>
        .top-left-lottie {
            position: absolute;
            top: 10px;
            left: 10px;
            z-index: 999;
            width: 200px;
        }
    </style>
    <div class="top-left-lottie" id="lottie-container"></div>
""", unsafe_allow_html=True)


# Streamlit page config
st.set_page_config(page_title="Mood App", layout="wide")

# Show the animation
st.title("How's your mood today?")
st_lottie(lottie_mood, height=300)
