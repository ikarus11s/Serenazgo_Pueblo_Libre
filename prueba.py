import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

def main():
    # Configuración de la página
    st.title("Acceso a Google Sheets con Streamlit")
    st.write("Esta aplicación permite leer y escribir datos en una hoja de cálculo de Google Sheets.")

    # Leer credenciales desde los secretos de Streamlit
    json_creds = st.secrets["gspread"]["json"]

    # Configuración de credenciales y acceso
    scope = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_dict(json_creds, scope)
    client = gspread.authorize(creds)

    try:
        # Acceso a la hoja de cálculo
        spreadsheet = client.open('Prueba')  # Nombre del documento de Google Sheets
        sheet = spreadsheet.worksheet('Hoja 1')  # Nombre de la hoja dentro del documento
        
        # Leer datos y convertir a DataFrame
        data = pd.DataFrame(sheet.get_all_records())
        st.write("Datos leídos desde Google Sheets:")
        st.dataframe(data)  # Usar st.dataframe() para una vista interactiva
        
        # Escribir datos
        if st.button('Agregar datos'):
            sheet.append_row(['Nuevo', 'Dato', 'Ejemplo'])
            st.write("Datos agregados exitosamente.")
        
    except gspread.SpreadsheetNotFound:
        st.error("No se pudo encontrar la hoja de cálculo. Verifica el nombre y el acceso.")
    except gspread.WorksheetNotFound:
        st.error("No se pudo encontrar la hoja dentro de la hoja de cálculo. Verifica el nombre de la hoja.")
    except Exception as e:
        st.error(f"Ocurrió un error: {e}")

if __name__ == "__main__":
    main()
