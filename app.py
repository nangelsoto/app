import streamlit as st
import cv2
import numpy as np
import pytesseract
from PIL import Image
from googletrans import Translator

translator = Translator()

# Configurar la ruta de Tesseract
pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'  # Ruta a la instalación de Tesseract en tu sistema

st.title("Reconocimiento óptico de Caracteres")

img_file_buffer = st.file_uploader("Toma una Foto", type=["png", "jpg", "jpeg"])

with st.sidebar:
    filtro = st.radio("Aplicar Filtro", ('Con Filtro', 'Sin Filtro'))

if img_file_buffer is not None:
    # To read image file buffer with PIL:
    image = Image.open(img_file_buffer)
    img_rgb = np.array(image)

    if filtro == 'Con Filtro':
        img_rgb = cv2.bitwise_not(img_rgb)

    text = pytesseract.image_to_string(img_rgb)

    # Translate the recognized text
    translated_text = translator.translate(text, dest='en').text
    st.write("Texto original:", text)
    st.write("Texto traducido:", translated_text)


