# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 17:32:18 2024

@author: MNahui
"""
import streamlit as st
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import folium
from folium import plugins

# Definimos los parámetros de configuración de la aplicación
st.set_page_config(
    page_title="Serenazgo de Pueblo Libre",  # Título de la página
    page_icon="📊",  # Ícono
    layout="wide",  # Forma de layout ancho o compacto
    initial_sidebar_state="expanded"  # Definimos si el sidebar aparece expandido o colapsado
)

gsheetid = '1gS6ZS6lS7Mc5B4TFI8HEK80xq4LANS6nU2O8V8-hEC8'
sheetid = '0'

url = f'https://docs.google.com/spreadsheets/d/{gsheetid}/export?format=csv&gid={sheetid}'

def cargar_datos_gsheet(url):
    """Carga los datos de Google Sheets y devuelve un DataFrame."""
    df = pd.read_csv(url)
    return df

def mostrar_mapa(df):
    """Muestra un mapa con los puntos de latitud y longitud del DataFrame."""
    # Crear un mapa centrado en las coordenadas medias
    m = folium.Map(location=[df['Latitud'].mean(), df['Longitud'].mean()], zoom_start=14, tiles='CartoDB positron')

    # Agregar puntos al mapa
    for idx, row in df.iterrows():
        folium.Marker(
            location=[row['Latitud'], row['Longitud']],
            popup=f'Fila: {idx + 1}',  # Número de fila
            icon=folium.Icon(color='blue')
        ).add_to(m)

    # Renderizar el mapa en Streamlit
    st.write(m._repr_html_(), unsafe_allow_html=True)

def obtener_datos():
    """Obtiene y muestra los datos y el mapa."""
    df = cargar_datos_gsheet(url)
    st.dataframe(df, use_container_width=True)
    mostrar_mapa(df)

# Ejecutar la función para obtener y mostrar los datos y el mapa
obtener_datos()


