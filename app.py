import streamlit as st
import requests
from streamlit_lottie import st_lottie

# Set page configuration
st.set_page_config(page_title="Mood Tracker", layout="centered")

# Load Lottie animation from URL
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Animation URL for "Free Emotions" animation
lottie_url = "https://lottie.host/f7f84b80-9de7-4b2e-b620-63d64c54a813/CTjzK45nCh.json"
lottie_json = load_lottieurl(lottie_url)

# Title and description
st.title("🧠 Mood Tracker")
st.write("Track your emotional health and visualize your mood transitions.")

# Show the animation
st_lottie(lottie_json, height=300, key="emotions")

# Optional: Mood input section
st.subheader("How are you feeling today?")
mood = st.radio("Choose your mood:", ["😊 Happy", "😐 Neutral", "😢 Sad", "😡 Angry", "😴 Tired"])

# Feedback
if st.button("Submit"):
    st.success(f"Mood recorded: {mood}")
