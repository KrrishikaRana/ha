
import streamlit as st
from streamlit_lottie import st_lottie
import json
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")

# Load lottie
def load_lottiefile(path: str):
    with open(path, "r") as f:
        return json.load(f)

mood_anim = load_lottiefile("jj.json")

# --- PAGE STATE ---
if "page" not in st.session_state:
    st.session_state.page = "home"  # default

# --- FUNCTIONS ---
def go_to_chart():
    st.session_state.page = "chart"

# --- PAGE 1: HOME ---
if st.session_state.page == "home":
    st.markdown("<h1 style='text-align:center;'>Mood check: vibin’ or surviving?</h1>", unsafe_allow_html=True)

    # Wrap animation with a "button" effect
    

    st_lottie(mood_anim, height=200, key="center_anim")

# --- PAGE 2: CHART ---
