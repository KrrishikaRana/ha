import streamlit as st
from streamlit_lottie import st_lottie
import json

# Page setup
st.set_page_config(page_title="Mood Detector", layout="wide")

# Load Lottie JSON
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

# Load animations
mood_anim = load_lottiefile("mood.json")           # Center animation
top_left_anim = load_lottiefile("jj.json")         # Top-left animation

# ----------------- CSS Styling -------------------
st.markdown(
    """
    <style>
    .stApp {
        background-color: #0d1117;
        color: white;
    }

    .top-left-lottie {
        position: fixed;
        top: 10px;
        left: 10px;
        width: 250px;
        height: 250px;
        z-index: 9999;
        pointer-events: none;
    }

    .form-box {
        background-color: #161b22;
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0 0 10px rgba(255, 255, 255, 0.1);
    }

    h1 {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --------- Inject Top-Left Lottie via HTML --------
from streamlit.components.v1 import html
html(f"""
    <div class="top-left-lottie">
        <lottie-player
            src='data:application/json;base64,{json.dumps(top_left_anim).encode("utf-8").decode("unicode_escape")}'
            background="transparent"
            speed="1"
            loop
            autoplay>
        </lottie-player>
    </div>
    <script src="https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js"></script>
""", height=0)

# --------------- Main Layout ---------------------
st.markdown("<h1 style='text-align: center;'>How's your mood today?</h1>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st_lottie(mood_anim, height=250, key="center_anim")

    st.markdown("<div class='form-box'>", unsafe_allow_html=True)
    with st.form("mood_form"):
        name = st.text_input("What's your name?")
        sleep_hours = st.slider("How many hours did you sleep?", 0, 12, 6)
        energy_level = st.radio("How energetic do you feel?", ["Low", "Medium", "High"])
        reason = st.text_area("What's the reason behind your current mood?")
        submitted = st.form_submit_button("Submit")
    st.markdown("</div>", unsafe_allow_html=True)

if "submitted" in locals() and submitted:
    st.success(f"Thanks {name}, let's check your mood...")

