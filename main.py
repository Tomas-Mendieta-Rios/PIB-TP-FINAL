import streamlit as st
from PIL import Image, ImageFilter, ImageOps
import os

image_folder_original = "Fotos"
processed_folder = "Fotos_Procesadas"
os.makedirs(processed_folder, exist_ok=True)

image_files_original = [f for f in os.listdir(image_folder_original) if f.lower().endswith(('png', 'jpg', 'jpeg'))]

st.sidebar.title("Opciones de Procesamiento")
filtros = st.sidebar.multiselect("Elige los filtros a aplicar (se aplicarán en orden):",["Escala de Grises", "Bordes", "Espejo Horizontal", "Invertir Colores"])

st.title("Procesamiento de Imágenes")

def aplicar_escala_grises(imagen):
    return ImageOps.grayscale(imagen)

def aplicar_bordes(imagen):
    return imagen.filter(ImageFilter.FIND_EDGES)

def aplicar_espejo_horizontal(imagen):
    return ImageOps.mirror(imagen)

def invertir_colores(imagen):
    return ImageOps.invert(imagen.convert("RGB"))

def aplicar_filtros(img, filtros_seleccionados):
    img_procesada = img.copy()
    for filtro in filtros_seleccionados:
        if filtro == "Escala de Grises":
            img_procesada = aplicar_escala_grises(img_procesada)
        elif filtro == "Bordes":
            img_procesada = aplicar_bordes(img_procesada)
        elif filtro == "Espejo Horizontal":
            img_procesada = aplicar_espejo_horizontal(img_procesada)
        elif filtro == "Invertir Colores":
            img_procesada = invertir_colores(img_procesada)
    return img_procesada

def plot(img_original, img_procesada):
    col1, col2 = st.columns(2)
    with col1:
        st.image(img_original, caption='Original', use_column_width=True)
    with col2:
        st.image(img_procesada, caption='Procesada', use_column_width=True)

def save_image(img_procesada, filename):
    save_path = os.path.join(processed_folder, filename)
    img_procesada.save(save_path)

def procesar(image_folder, image_files, filtros):
    for filename in image_files:
        img_path = os.path.join(image_folder, filename)
        img_original = Image.open(img_path)
        
        img_procesada = aplicar_filtros(img_original, filtros)
        
        plot(img_original, img_procesada)
        save_image(img_procesada, filename)


procesar(image_folder_original, image_files_original, filtros)


#streamlit run '/Users/tomasmendietarios/Library/Mobile Documents/com~apple~CloudDocs/I.T.B.A/Cuatri/PIM/TP_FINAL/main.py'