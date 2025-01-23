import streamlit as st
from audiorecorder import audiorecorder

st.title('SpeechBrain - Speech to Text')
st.write('Hello world')
audio = audiorecorder("Click to record", "Click to stop recording")

if len(audio) > 0:

    
    st.audio(audio.export().read(), autoplay=True) 
    
