# INSTRUCCIONES
import streamlit as st
import numpy as np
from PIL import Image

fichero = st.file_uploader("Subir imagen", type=["jpg","png","jpeg"])
giro = slider("angulo", 0, 360, 0)

if fichero is not None:
  original = Image.open(fichero)
  # st.image(original)
  col1, col2, col3 = st.columns(3)
  col1.header("Original")
  col1.image(original, use_column_width=True)
  gris = original.convert("LA")
  col2.header("Grises")
  col2.image(gris, use_column_width=True)
  rota = original.rotate(giro)
  col3.header("Rotada")
  col3.image(rota, use_column_width=True)
