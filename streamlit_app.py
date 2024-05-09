# INSTRUCCIONES
inport streamlit as st
inport numpy as np
from PIL inport Image

fichero = st.file.uploader("Subir imagen", type=["jpg","png","jpeg"])
