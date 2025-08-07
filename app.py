import streamlit as st
from streamlit_lottie import st_lottie
import json

# Set page config
st.set_page_config(page_title="Mood Detector", layout="wide")

# Load animation
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

lottie_anim = load_lottiefile("jj.json")

# Background styling
st.markdown(
    """
    <style>
    .stApp {
        background-color: #0d1117; /* dark mode */
        color: white;
    }
    h1 {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    .form-box {
        background-color: #161b22;
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0 0 10px rgba(255, 255, 255, 0.1);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Centered title
st.markdown("<h1 style='text-align: center;'>How's your mood today?</h1>", unsafe_allow_html=True)

# Centered layout
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st_lottie(lottie_anim, height=200, key="moodAnim")

    with st.container():
        st.markdown("<div class='form-box'>", unsafe_allow_html=True)

        with st.form("mood_form"):
            name = st.text_input("What's your name?")
            sleep_hours = st.slider("How many hours did you sleep?", 0, 12, 6)
            energy_level = st.radio("How energetic do you feel?", ["Low", "Medium", "High"])
            reason = st.text_area("What's the reason behind your current mood?")
            submitted = st.form_submit_button("Submit")

        st.markdown("</div>", unsafe_allow_html=True)

if submitted:
    st.success(f"Thanks {name}, let's check your mood...")
