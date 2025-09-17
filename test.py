# Se Importaron las librerias que se van a usar
import streamlit as st
from PIL import Image

# diseño de la interfaz

# creacion del sidebar
logouich = Image.open("images/v2Logo.png")
halcon = Image.open("images/mascota sin fondo reflejo.png")

with st.sidebar:
    st.image(logouich, width= 300)
    st.markdown("<h1 style='text-align: center; margin-top: 0; padding-top:0 '>Instrucciones:</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Dentro del recuadro oscuro"
    " escribe una pregunta con respecto a la universidad como cuales son los papeles necesarios"
    " para inscribirse, precios de cuotas, etc.</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-style: italic; font-size: 0.8em; padding-top: 20px; margin-bottom: 0; padding-bottom: 0;'>@UICh 2025 Copyright</p>", unsafe_allow_html=True)
    st.image(halcon, width= 350)

# Titulos y texto explicativo
st.set_page_config(page_title="UIEPCh", page_icon="🤖")
st.markdown("<h1 style='text-align: center; font-size: 4em;'>Hola, estudiante</h1>", unsafe_allow_html=True)
st.text("Soy el asistente virtual oficial de la UICh, en que puedo ayudarte :D")

# Area del prompt
chat_placeholder = st.container()
prompt_placeholder = st.form("chat-form")

with prompt_placeholder:
    st.markdown("**Chat**  -  _presiona Enter para enviar_")
    cols = st.columns((6, 1))
    cols[0].text_input(
        "Chat",
        placeholder="Pregunta a UIChito",
        label_visibility="collapsed",
    )
    cols[1].form_submit_button(
        "Enviar", 
        type="primary",
    )


