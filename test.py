import streamlit as st
from PIL import Image
##print("esto es una prueba")

st.set_page_config(page_title="UIEPCh", page_icon="🤖")
st.title('¡Hola Estudiante! 🐔')
st.text("Soy el asistente virtual oficial de la UICh, responderé a cualquier duda que tengas con respecto a la universidad ¿En qué puedo ayudarte? :)")

chat_placeholder = st.container()
prompt_placeholder = st.form("chat-form")

with prompt_placeholder:
    st.markdown("**Chat**  -  _presiona Enter para enviar_")
    cols = st.columns((6, 1))
    cols[0].text_input(
        "Chat",
        value="Hola",
        label_visibility="collapsed",
    )
    cols[1].form_submit_button(
        "Enviar", 
        type="primary",
    )



##crear un entorno virtual venv
##instalar dependencias
##pip install streamlit en la terminal del proyecto
##



