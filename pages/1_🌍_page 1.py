import streamlit as st
from audiorecorder import audiorecorder
st.set_page_config(page_title="Page 1", page_icon="🌍")



st.title("Audio Recorder")

audio=audiorecorder(start_prompt="Start recording", stop_prompt="Stop recording", pause_prompt="Pause", key=None)
if len(audio) > 0:
    # To play audio in frontend:
    st.audio(audio.export().read())  

    # To save audio to a file, use pydub export method:
    audio.export("audio.wav", format="wav")

    # To get audio properties, use pydub AudioSegment properties:
    st.write(f"Frame rate: {audio.frame_rate}, Frame width: {audio.frame_width}, Duration: {audio.duration_seconds} seconds")