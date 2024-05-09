# INSTRUCCIONES
import streamlit as st
import numpy as np
from PIL import Image

fichero = st.file.uploader("Subir imagen", type=["jpg","png","jpeg"])
