# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 17:32:18 2024

@author: MNahui
"""
import streamlit as st
import pandas as pd

# Definimos los parámetros de configuración de la aplicación
st.set_page_config(
    page_title="Demo carga datos desde Google Sheets", #Título de la página
    page_icon="📊", # Ícono
    layout="wide", # Forma de layout ancho o compacto
    initial_sidebar_state="expanded" # Definimos si el sidebar aparece expandido o colapsado
)


gsheetid='1gS6ZS6lS7Mc5B4TFI8HEK80xq4LANS6nU2O8V8-hEC8'
sheetid='0'


url = f'https://docs.google.com/spreadsheets/d/{gsheetid}/export?format=csv&gid={sheetid}&format'



@st.experimental_fragment(run_every=5)
def Cargar_Datos(url):
    dfDatos = pd.read_csv(url)
    st.dataframe(dfDatos,use_container_width=True)
    

@st.experimental_fragment(run_every=5)
def Cargar_mapa(url):
    dfDatos = pd.read_csv(url)
    coordenadas = dfDatos[['Latitud','Longitud']]
    coordenadas.columns = ['lat','lon']
    st.map(coordenadas,size = [1.0] ,color = '#00ff00'  )


Cargar_mapa(url)

