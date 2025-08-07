from streamlit_lottie import st_lottie
import streamlit as st
pip install streamlit-lottie


st.set_page_config(page_title="Mood Detector", layout="centered")

# Custom CSS to change background color
st.markdown(
    """
    <style>
    .stApp {
        background-color: #87CEEB; /* Sky blue hex */
    }
    </style>
    """,
    unsafe_allow_html=True
)


import json

# Function to load your Lottie animation
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

# Load your animation (make sure 'mood.json' is in the same folder)
lottie_animation = load_lottiefile("jj.json")

# Optional: Page config
st.set_page_config(page_title="My App", page_icon="✨", layout="wide")

# Use columns to align animation to the top left
col1, col2 = st.columns([1, 5])  # You can tweak width ratio if needed

with col1:
    st_lottie(lottie_anim, height=200)


with col2:
   
    col1, col2, col3 = st.columns([1, 2, 1])  # Center column is twice as big

with col2:
    st.title("How's your mood today?")
    with st.form("mood_form"):
      name = st.text_input("What's your name?")
      sleep_hours = st.slider("How many hours did you sleep?", 0, 12, 6)
      energy_level = st.radio("How energetic do you feel?", ["Low", "Medium", "High"])
      reason = st.text_area("What's the reason behind your current mood?")
    
    submitted = st.form_submit_button("Submit")

if submitted:
    st.success(f"Thanks {name}, let's check your mood...")
    # Call prediction logic here

   
# Add more sections below as needed

