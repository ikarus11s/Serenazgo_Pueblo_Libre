# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 17:32:18 2024

@author: MNahui
"""


import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

# URL de la hoja de cálculo
url = "https://docs.google.com/spreadsheets/d/1gS6ZS6lS7Mc5B4TFI8HEK80xq4LANS6nU2O8V8-hEC8/edit?usp=sharing"

# Conexión con Google Sheets
conn = st.experimental_connection("gsheets", type=GSheetsConnection)

# Leer el rango específico: primeras 10 columnas (A-J) hasta la fila 50
range_ = 'A1:J50'
data = conn.read(spreadsheet=url, range_=range_)

# Convertir los datos a un DataFrame de pandas
df = pd.DataFrame(data)

# Mostrar los datos
st.dataframe(df)
