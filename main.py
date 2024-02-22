import streamlit as st
from audiorecorder import audiorecorder

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.sidebar.success("Select a page above.")