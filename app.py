# Se Importaron las librerias que se van a usar
from dataclasses import dataclass
from typing import Literal
import streamlit as st

from langchain_classic.callbacks import get_openai_callback
from langchain_openai import ChatOpenAI
from langchain_classic.chains.conversation.memory import ConversationSummaryMemory
from langchain_classic.chains.conversation.base import ConversationChain
#import streamlit.components.v1 as components

from PIL import Image


@dataclass
class Message:
    """Class for keeping track of a chat message."""
    origin: Literal["human", "ai"]
    message: str


#Creacion de la funcion sesion_state
def initialize_session_state():
    if "history" not in st.session_state:
        st.session_state.history = []
    if "conversation" not in st.session_state:
        chat_llm = ChatOpenAI(
            temperature = 0,
            openai_api_key = st.secrets["openai_api_key"],
            model_name= "gpt-5-nano"
        )

        st.session_state.conversation = ConversationChain(
            llm = chat_llm,
            memory = ConversationSummaryMemory(llm = chat_llm),
        )


#Funcion de callback para los mensajes
def on_click_callback():
    human_prompt = st.session_state.human_prompt
    llm_response = st.session_state.conversation.run( 
        human_prompt
    )
    st.session_state.history.append(
        Message("human", human_prompt)
    )
    st.session_state.history.append(
        Message("ai", llm_response)
    )

initialize_session_state()

#########################################################################################################################

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

with chat_placeholder:
    for chat in st.session_state.history:
        st.markdown(f"From {chat.origin}: {chat.message}")

with prompt_placeholder:
    st.markdown("**Chat**  -  _presiona Enter para enviar_")
    cols = st.columns((6, 1))
    cols[0].text_input(
        "Chat",
        placeholder="Pregunta a UIChito",
        label_visibility="collapsed",
        key="human_prompt",
    )
    cols[1].form_submit_button(
        "Enviar", 
        type="primary",
        on_click=on_click_callback, 
    )

# logica 

# callbacks

