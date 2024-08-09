# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 17:32:18 2024

@author: MNahui
"""


import streamlit as st
from streamlit_gsheets import GSheetsConnection

# Create a connection object.
conn = st.connection("gsheets", type=GSheetsConnection)

df = conn.read(
    worksheet="Hoja 1",
    ttl="10m",
    usecols=[0, 7],
    nrows=20,
)

# Print results.
for row in df.itertuples():
    st.write(f"{row.name} has a :{row.pet}:")