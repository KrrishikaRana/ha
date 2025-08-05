import streamlit as st
from streamlit_lottie import st_lottie
import requests

# Function to fetch animation JSON from a URL
def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Load Lottie animation
lottie_url = "https://assets10.lottiefiles.com/packages/lf20_0yfsb3a1.json"  # mood-related animation
lottie_json = load_lottie_url(lottie_url)

# Streamlit UI
st.markdown("<h1 style='text-align: center;'>Mood Tracker</h1>", unsafe_allow_html=True)
st_lottie(lottie_json, height=300, key="emotions")
