import streamlit as st
from streamlit_lottie import st_lottie
import requests

# Function to load the Lottie animation from a URL
def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Load a Lottie animation (this one is a guy waving, but you can change the URL)
lottie_animation = load_lottie_url("https://assets4.lottiefiles.com/packages/lf20_ZV1fn5lhl.json")

# Set page config
st.set_page_config(page_title="Mood Tracker", page_icon="🧠", layout="centered")

# Centered title
st.markdown("<h1 style='text-align: center;'>Mood Tracker App</h1>", unsafe_allow_html=True)

# Centered subtitle
st.markdown("<h3 style='text-align: center;'>Track your emotions daily ✨</h3>", unsafe_allow_html=True)

# Add some spacing
st.write("")
st.write("")

# Show Lottie animation centered
st_lottie(lottie_animation, height=300, key="mood")

