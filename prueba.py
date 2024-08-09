# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 17:32:18 2024

@author: MNahui
"""


import streamlit as st
from streamlit_gsheets import GSheetsConnection

url = "https://docs.google.com/spreadsheets/d/1gS6ZS6lS7Mc5B4TFI8HEK80xq4LANS6nU2O8V8-hEC8/edit?usp=sharing"

conn = st.experimental_connection("gsheets", type=GSheetsConnection)

data = conn.read(spreadsheet=url)



st.dataframe(data)