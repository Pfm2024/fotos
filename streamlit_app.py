# INSTRUCCIONES
import streamlit as st
import numpy as np
from PIL import Image

fichero = st.file_uploader("Subir imagen", type=["jpg","png","jpeg"])

if fichero is not None:
  original = Image.open(fichero)
  st.image(original)
