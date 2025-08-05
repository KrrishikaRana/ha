import streamlit as st
from streamlit_lottie import st_lottie
import requests

st.set_page_config(page_title="Mood Tracker", layout="wide")

# Function to load Lottie animations from URL
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Load multiple Lottie animations
lottie_mood = load_lottieurl("https://lottie.host/5db20f7e-f178-46c5-92f2-92c6e85c0d20/qPGzRPGzFg.json")
lottie_peace = load_lottieurl("https://lottie.host/bf70189a-bc33-42cb-8225-c69bb5a4d5f8/1cCLTb8mrG.json")
lottie_flower = load_lottieurl("https://lottie.host/5e44a7d1-d61a-45f7-bd94-e8c157eb660c/5Hv93fK1NY.json")
lottie_nature = load_lottieurl("https://lottie.host/843a8853-91a7-48de-a364-dc891dfafad4/vSL0r8vruW.json")
lottie_bloom = load_lottieurl("https://lottie.host/c6df849e-cc13-4c33-80a8-5bfa878dcb9b/RSkHZKRGwB.json")

# Title
st.markdown("<h1 style='text-align: center;'>🌿 Mood Garden 🌿</h1>", unsafe_allow_html=True)

# Layout in columns for multiple animations
col1, col2, col3 = st.columns(3)
with col1:
    st_lottie(lottie_mood, height=200, key="mood")

with col2:
    st_lottie(lottie_peace, height=200, key="peace")

with col3:
    st_lottie(lottie_flower, height=200, key="flower")

col4, col5 = st.columns(2)
with col4:
    st_lottie(lottie_nature, height=200, key="nature")

with col5:
    st_lottie(lottie_bloom, height=200, key="bloom")
