from st_audiorec import st_audiorec
import streamlit as st
from utils.voice_handler import voice_to_text


wav_audio_data = st_audiorec()


if wav_audio_data is not None:
    st.audio(wav_audio_data, format='audio/wav')
    
    with open("music.wav", "wb") as f:
        f.write(wav_audio_data)
    
    
