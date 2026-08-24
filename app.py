import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Mes Jeux", layout="wide")

# Lire le fichier HTML
with open("index.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# Afficher le HTML
components.html(html_content, height=900, scrolling=True)
