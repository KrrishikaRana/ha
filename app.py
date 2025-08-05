import streamlit as st
from streamlit_lottie import st_lottie
import json

# Function to load your Lottie animation
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

# Load your animation (make sure 'mood.json' is in the same folder)
lottie_animation = load_lottiefile("mood.json")

# Optional: Page config
st.set_page_config(page_title="My App", page_icon="✨", layout="wide")

# Use columns to align animation to the top left
col1, col2 = st.columns([1, 5])  # You can tweak width ratio if needed

with col1:
    st_lottie(lottie_animation, height=200)

with col2:
    st.markdown("### Welcome to the App")
    st.write("This is your Streamlit application with a top-left animation.")

# Add more sections below as needed
st.write("Add your widgets, logic, and content below here.")
