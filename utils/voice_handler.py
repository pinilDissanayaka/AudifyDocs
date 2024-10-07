import os
import streamlit as st
from groq import Groq

os.environ['GROQ_API_KEY']=st.secrets['GROQ_API_KEY']

def save_voice_on_dir(folder, voice_file, format=".wav"):
    
    with open(voice_file, "wb") as music_file:
        
        
    

def voice_to_text(voice_file): 
    client=Groq()
    
    transcription = client.audio.transcriptions.create(
        file=voice_file, # Required audio file
        model="distil-whisper-large-v3-en", # Required model to use for transcription
        prompt="Specify context or spelling",  # Optional
        response_format="json",  # Optional
        language="en",  # Optional
        temperature=0.0  # Optional
    )

    print(transcription.text)