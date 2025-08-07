import streamlit as st
from streamlit_lottie import st_lottie
import json

# Page setup
st.set_page_config(page_title="Mood Detector", layout="wide")

# Load Lottie animation from file
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

# Load two animations
top_left_anim = load_lottiefile("jj.json")    # Top-left
mood_anim = load_lottiefile("mood.json")      # Centered

# CSS Styling
st.markdown(
    """
    <style>
    .stApp {
        background-color: #0d1117;
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
    .top-left {
        position: absolute;
        top: 10px;
        left: 10px;
        width: 200px;
        z-index: 999;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Top-left animation
st.markdown('<div class="top-left">', unsafe_allow_html=True)
st_lottie(top_left_anim, height=100, key="top_left")
st.markdown('</div>', unsafe_allow_html=True)

# Centered Heading
st.markdown("<h1 style='text-align: center;'>How's your mood today?</h1>", unsafe_allow_html=True)

# Centered layout
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st_lottie(mood_anim, height=200, key="center_anim")

    with st.container():
        st.markdown("<div class='form-box'>", unsafe_allow_html=True)

        with st.form("mood_form"):
            name = st.text_input("What's your name?")
            sleep_hours = st.slider("How many hours did you sleep?", 0, 12, 6)
            energy_level = st.radio("How energetic do you feel?", ["Low", "Medium", "High"])
            reason = st.text_area("What's the reason behind your current mood?")
            submitted = st.form_submit_button("Submit")

        st.markdown("</div>", unsafe_allow_html=True)

# Mood analysis result
if submitted:
    st.success(f"Thanks {name}! 👋")

    # Mood logic
    if sleep_hours < 5 or energy_level == "Low":
        mood_status = "😴 You might be feeling tired or low. Take care and get some rest!"
    elif energy_level == "High" and sleep_hours >= 7:
        mood_status = "🔥 You're on fire today! Keep slaying 💪"
    else:
        mood_status = "🙂 You're doing okay. Stay balanced and hydrate 💧"

    st.markdown(f"### Mood Summary: {mood_status}")
    if reason.strip():
        st.info(f"Reason noted: _{reason}_")
    else:
        st.warning("You didn’t mention the reason behind your mood.")


