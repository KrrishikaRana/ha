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
   # Top-left
mood_anim = load_lottiefile("jj.json") 
top_left_anim = load_lottiefile("mood.json") # Centered

# CSS Styling
st.markdown(
    """
    <div style="position: fixed; top: 0; left: 0; z-index: 9999; width: 200px;">
        <div id="lottie-container"></div>
    </div>
    """,
    unsafe_allow_html=True
)

# Show the animation *inside the container*
st_lottie(top_left_anim, height=200, width=200, key="floating")
# Centered Heading
st.markdown("<h1 style='text-align: center;'>How's your mood today?</h1>", unsafe_allow_html=True)

# Centered layout
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st_lottie(mood_anim, height=500, key="center_anim")

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


