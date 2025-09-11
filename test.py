import streamlit as st
from PIL import Image
##print("esto es una prueba")

st.set_page_config(page_title="UIEPCh", page_icon="🤖")
st.title('¡Hola Estudiante! 🐔')
st.text("Soy el asistente vitual oficial de la UICh, respondere a cualquier duda que tengas con respecto a la universidad ¿En que puedo ayudarte?  :)")

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



##crear un entorno virtual evnv
##instalar dependencias
##pip install streamlit__ en la terminal del proyecto



