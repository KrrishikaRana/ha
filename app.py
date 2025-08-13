import streamlit as st
from streamlit_lottie import st_lottie
import json
import random

st.set_page_config(layout="wide")

# --- Load lottie function ---
def load_lottiefile(path: str):
    with open(path, "r") as f:
        return json.load(f)

# --- Animations ---
mood_anim = load_lottiefile("jj.json")
extra_anim = load_lottiefile("mood.json") 

# --- Random motivational lines ---
genz_lines = [
    ("Serving moods, not excuses", "#8be9fd"),
    ("Main character energy only 💫", "#8be9fd"),
    ("If your vibe is broken, we got the glue 🛠️", "#50fa7b"),
    ("Cry a little, slay a lot 💅", "#bd93f9"),
    ("Zero mood swings, only plot twists 📖✨", "#8be9fd"),
    ("We don’t do bad days, only side quests 🎯", "#8be9fd"),
]
random_line, random_color = random.choice(genz_lines)

# --- Top small animation ---
st.markdown(
    """
    <div style="position: fixed; top: 0; left: 0; z-index: 9999;">
    """,
    unsafe_allow_html=True
)
st_lottie(extra_anim, key="extra_anim", height=80, width=120)
st.markdown("</div>", unsafe_allow_html=True)

# --- Motivational line ---
st.markdown(
    f"""
    <div style="text-align:center;">
        <h2 style='
            color: {random_color}; 
            font-family: "Comic Sans MS", "Segoe UI", sans-serif;
            text-shadow: 2px 2px 8px rgba(0,0,0,0.3);
            display: inline-block;
        '>
            {random_line}
        </h2>
    </div>
    """,
    unsafe_allow_html=True
)

# --- Mood animation under the text ---
st.markdown("<div style='text-align:center;'>", unsafe_allow_html=True)
st_lottie(mood_anim, height=300, key="center_anim")
st.markdown("</div>", unsafe_allow_html=True)
<div style="position: fixed; bottom: 20px; right: 20px;">
    <iframe width="200" height="113" 
        src="https://www.youtube.com/embed/jfKfPfyJRdk?autoplay=1&loop=1&playlist=jfKfPfyJRdk" 
        frameborder="0" 
        allow="autoplay; encrypted-media" 
        allowfullscreen>
    </iframe>
</div>

