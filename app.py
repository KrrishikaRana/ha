
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
    st.markdown("<h1 style='text-align:center;'>Mood Detector</h1>", unsafe_allow_html=True)

    # Wrap animation with a "button" effect
    if st.button("📊 View Mood Tracker Chart"):
        go_to_chart()

    st_lottie(mood_anim, height=200, key="center_anim")

# --- PAGE 2: CHART ---
elif st.session_state.page == "chart":
    st.markdown("## 📈 Mood Tracking History")

    # Fake data for demo
    df = pd.DataFrame({
        "Date": pd.date_range(start="2025-08-01", periods=7),
        "Mood Score": [6, 7, 8, 5, 9, 6, 7]
    })

    # Plot
    fig, ax = plt.subplots()
    ax.plot(df["Date"], df["Mood Score"], marker='o')
    ax.set_xlabel("Date")
    ax.set_ylabel("Mood Score (1-10)")
    ax.set_title("Mood Tracker Over Time")
    st.pyplot(fig)

    if st.button("⬅ Back"):
        st.session_state.page = "home"


