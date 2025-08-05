import streamlit as st
st.markdown("""
    <style>
    .stApp {
        background-color: #f5f5f5;
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
lottie_mood = load_lottiefile("mood.json")
lottie_mood = load_lottiefile("jj.json")

# Streamlit page config
st.set_page_config(page_title="Mood App", layout="wide")

# Show the animation
st.title("How's your mood today?")
st_lottie(lottie_mood, height=300)
