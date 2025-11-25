# Se Importaron las librerias que se van a usar
from dataclasses import dataclass
from typing import Literal
import streamlit as st


#from langchain_classic.memory import ConversationBufferWindowMemory
from langchain_community.vectorstores import Chroma
from langchain_classic.callbacks import get_openai_callback
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_classic.chains.conversation.memory import ConversationSummaryMemory
from langchain_classic.chains.conversation.base import ConversationChain
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
#import streamlit.components.v1 as components

from PIL import Image

#carga de documentos
@st.cache_resource
def load_pdf():
    pdf_name = 'descripcion_tesis.pdf'
    loader = PyPDFLoader(pdf_name)
    docs = loader.load() 

#dividir texto en fragmentos
    text_splitter = RecursiveCharacterTextSplitter(chunk_size = 1000, chunk_overlap = 200) 
    chunked_document = text_splitter.split_documents(docs)

#creacion de la db
    vectordb = Chroma.from_documents(
        chunked_document, OpenAIEmbeddings(model="text-embedding-3-large", api_key= st.secrets["openai_api_key"])
    )
    return vectordb





@dataclass
class Message:
    """Class for keeping track of a chat message."""
    origin: Literal["human", "ai"]
    message: str

#probar
def load_css():
    with open("static/styles.css", "r") as f:
        css = f"<style>{f.read()}</style>"
        st.markdown(css, unsafe_allow_html=True)


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
#probar
load_css()
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
st.markdown("<h1 style='text-align: center; font-size: 4em;'>Hola, Futuro halcón</h1>", unsafe_allow_html=True)
st.text("Soy el asistente virtual oficial de la UICh, en que puedo ayudarte :D")

# Area del prompt
chat_placeholder = st.container()
prompt_placeholder = st.form("chat-form")

with chat_placeholder:
    ##probar
    for chat in st.session_state.history:
        div = f"""
<div class="chat-row 
    {'' if chat.origin == 'ai' else 'row-reverse'}">
    <img class="chat-icon" src="app/static/{
        'halcon (1).png' if chat.origin == 'ai' 
                      else 'perfil.png'}"
         width=32 height=32>
    <div class="chat-bubble
    {'ai-bubble' if chat.origin == 'ai' else 'human-bubble'}">
        &#8203;{chat.message}
    </div>
</div>       
        """
        st.markdown(div, unsafe_allow_html=True)

    for _ in range(3):
        st.markdown("")

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

#probar
