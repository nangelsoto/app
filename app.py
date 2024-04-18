import streamlit as st
import cv2
import numpy as np
import pytesseract
from PIL import Image

st.title("Reconocimiento óptico de Caracteres")

img_file_buffer = st.camera_input("Toma una Foto")

with st.sidebar:
    filtro = st.radio("Aplicar Filtro", ('Con Filtro', 'Sin Filtro'))

if img_file_buffer is not None:
    # Leer el buffer de la imagen con OpenCV
    bytes_data = img_file_buffer.getvalue()
    cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)
    
    if filtro == 'Con Filtro':
        cv2_img = cv2.bitwise_not(cv2_img)
    else:
        cv2_img = cv2_img
    
    # Convertir la imagen a RGB y extraer el texto
    img_rgb = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2RGB)
    text = pytesseract.image_to_string(img_rgb)
    
    # Mostrar la imagen
    st.image(img_rgb, caption='Imagen Capturada', use_column_width=True)
    
    # Mostrar el texto debajo de la imagen
    st.write("Caracteres encontrados:")
    st.write(text)



