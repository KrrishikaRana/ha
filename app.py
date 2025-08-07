import streamlit as st
from streamlit_lottie import st_lottie
import json

# Page configuration
st.set_page_config(page_title="Mood Detector", page_icon="✨", layout="wide")

# Custom CSS for background
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

# Function to load your Lottie animation from a local JSON file
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

# Load the animation
lottie_animation = load_lottiefile("jj.json")  # Make sure jj.json is in the same directory

# Layout: Lottie on the left, form on the right
col1, col2 = st.columns([1, 5])

with col1:
    st_lottie(lottie_animation, height=200)

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
        st.write(f"**Sleep Hours:** {sleep_hours}")
        st.write(f"**Energy Level:** {energy_level}")
        st.write(f"**Mood Reason:** {reason}")
