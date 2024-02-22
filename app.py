import streamlit as st
import os
import time
import glob
from gtts import gTTS
from PIL import Image

st.title("Interfaces Multimodales.")
image = Image.open('text_to_audio.png')

st.image(image, width=200)
