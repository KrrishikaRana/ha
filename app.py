
import streamlit as st
from streamlit_lottie import st_lottie
import json
import random

st.set_page_config(layout="wide")

# Load lottie
def load_lottiefile(path: str):
    with open(path, "r") as f:
        return json.load(f)

mood_anim = load_lottiefile("jj.json")

# --- GEN Z MOTIVATIONAL LINES ---
genz_lines = [
    ("Serving moods, not excuses ", "#8be9fd"),
    ("Main character energy only 💫", "#8be9fd"),
    ("If your vibe is broken, we got the glue 🛠️", "#8be9fd"),
    ("Cry a little, slay a lot 💅", "#bd93f9"),
    ("Zero mood swings, only plot twists 📖✨", "#8be9fd"),
    ("We don’t do bad days, only side quests 🎯", "#8be9fd"),
  
]
random_line, random_color = random.choice(genz_lines)

# --- PAGE ---

# Aesthetic Gen Z line in center
st.markdown(
    f"""
    <h2 style='
        text-align: center; 
        color: {random_color}; 
        font-family: "Comic Sans MS", "Segoe UI", sans-serif;
        text-shadow: 2px 2px 8px rgba(0,0,0,0.3);
    '>
        {random_line}
    </h2>
    """,
    unsafe_allow_html=True
)

# Mood animation centered
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st_lottie(mood_anim, height=600, key="center_anim")
