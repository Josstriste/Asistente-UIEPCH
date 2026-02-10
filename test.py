import streamlit as st
import os
from dataclasses import dataclass
from typing import Literal
from PIL import Image

# Importaciones de LangChain
from langchain_chroma import Chroma
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_classic.chains.conversational_retrieval.base import ConversationalRetrievalChain
from langchain_classic.chains.conversation.memory import ConversationSummaryMemory

# Configuración de la página
st.set_page_config(page_title="UIEPCh", page_icon="🤖")

# Constantes
# Nombre de la carpeta donde se guardará la base de datos vectorial
PERSIST_DIRECTORY = "./chroma_db"
# Nombre del archivo pdf
PDF_PATH = "vectordatabase.pdf"

@dataclass
class Message:
    """Class for keeping track of a chat message."""
    origin: Literal["human", "ai"]
    message: str

def load_css():
    if os.path.exists("static/styles.css"):
        with open("static/styles.css", "r") as f:
            css = f"<style>{f.read()}</style>"
            st.markdown(css, unsafe_allow_html=True)

# Función para preparar la Base de Datos Vectorial para el sistema RAG
@st.cache_resource
def get_vectorstore():
    """
    Carga el PDF, lo convierte en embeddings y lo guarda en disco (Chroma).
    Si ya existe en disco, lo carga directamente para ahorrar dinero y tiempo.
    """
    
    # Definir los embeddings (usamos OpenAI)
    embedding_function = OpenAIEmbeddings(openai_api_key=st.secrets["openai_api_key"])

    # Verificar si ya existe la base de datos persistente
    if os.path.exists(PERSIST_DIRECTORY) and os.listdir(PERSIST_DIRECTORY):
        print("Base de datos encontrada. Cargando...")
        vectorstore = Chroma(persist_directory=PERSIST_DIRECTORY, embedding_function=embedding_function)
    else:
        print("Base de datos no encontrada. Creando a partir del PDF...")
        if not os.path.exists(PDF_PATH):
            st.error(f"No se encontró el archivo {PDF_PATH}. Por favor agrégalo al proyecto.")
            return None
            
        # 1. Cargar el PDF
        loader = PyPDFLoader(PDF_PATH)
        documents = loader.load()
        
        # 2. Dividir el texto (Split)
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,  # Tamaño del fragmento
            chunk_overlap=200 # Solapamiento para mantener contexto
        )
        chunks = text_splitter.split_documents(documents)
        
        # 3. Crear VectorStore y guardar en disco
        vectorstore = Chroma.from_documents(
            documents=chunks,
            embedding=embedding_function,
            persist_directory=PERSIST_DIRECTORY
        )
        print("Base de datos creada y guardada.")
        
    return vectorstore

def initialize_session_state():
    if "history" not in st.session_state:
        st.session_state.history = []
        
    # Inicializar la cadena solo si no existe
    if "conversation" not in st.session_state:
        
        # Obtener la base de datos vectorial
        vectorstore = get_vectorstore()
        
        if vectorstore:
            # Configurar el LLM
            chat_llm = ChatOpenAI(
                temperature=0,
                openai_api_key=st.secrets["openai_api_key"],
                model_name="gpt-4o-mini", 
                max_tokens=400
            )

            # Configurar la memoria (resumen de la conversación)
            memory = ConversationSummaryMemory(
                llm=chat_llm, 
                memory_key="chat_history", 
                return_messages=True,
                output_key="answer"
            )

            # Crear la cadena RAG (ConversationalRetrievalChain)
            st.session_state.conversation = ConversationalRetrievalChain.from_llm(
                llm=chat_llm,
                retriever=vectorstore.as_retriever(search_kwargs={"k": 3}), # Busca los 3 fragmentos más relevantes
                memory=memory,
                verbose=True # Para ver en consola qué está pasando
            )

def on_click_callback():
    human_prompt = st.session_state.human_prompt
    
    if st.session_state.conversation:
        # Ejecutar la cadena con la pregunta del usuario
        # Nota: ConversationalRetrievalChain espera un diccionario con "question"
        response = st.session_state.conversation.invoke({"question": human_prompt})
        
        llm_response = response['answer']

        st.session_state.history.append(
            Message("human", human_prompt)
        )

        st.session_state.history.append(
            Message("ai", llm_response)
        )

# Ejecución Principal
load_css()
initialize_session_state()

# Diseño del Sidebar
try:
    if os.path.exists("images/v2Logo.png"):
        logouich = Image.open("images/v2Logo.png")
        st.sidebar.image(logouich, width=300)
        
    st.sidebar.markdown("<h1 style='text-align: center; margin-top: 0; padding-top:0 '>Instrucciones:</h1>", unsafe_allow_html=True)
    st.sidebar.markdown("<p style='text-align: center;'>Dentro del recuadro oscuro"
        " escribe una pregunta con respecto a la universidad como cuales son los papeles necesarios"
        " para inscribirse, precios de cuotas, etc.</p>", unsafe_allow_html=True)
    st.sidebar.markdown("<p style='text-align: center; font-style: italic; font-size: 0.8em; padding-top: 20px; margin-bottom: 0; padding-bottom: 0;'>@UICh 2025 Copyright</p>", unsafe_allow_html=True)
    
    if os.path.exists("images/mascota sin fondo reflejo.png"):
        halcon = Image.open("images/mascota sin fondo reflejo.png")
        st.sidebar.image(halcon, width=350)
except Exception as e:
    st.sidebar.warning("Imágenes no encontradas. Verifica las rutas.")

# Interfaz Principal
st.markdown("<h1 style='text-align: center; font-size: 4em;'>Hola, Futuro halcón</h1>", unsafe_allow_html=True)
st.text("Soy el asistente virtual oficial de la UICh, en que puedo ayudarte :D")

chat_placeholder = st.container()
prompt_placeholder = st.form("chat-form")

with chat_placeholder:
    for chat in st.session_state.history:
        
        icon_path = 'app/static/halcon (1).png' if chat.origin == 'ai' else 'perfil.png'
        
        div = f"""
        <div class="chat-row {'' if chat.origin == 'ai' else 'row-reverse'}">
            <div class="chat-icon" style="font-size:32px">
                {'🤖' if chat.origin == 'ai' else '👤'}
            </div>
            <div class="chat-bubble {'ai-bubble' if chat.origin == 'ai' else 'human-bubble'}">
                &#8203;{chat.message}
            </div>
        </div>
        """
        st.markdown(div, unsafe_allow_html=True)

    for _ in range(3):
        st.markdown("")

with prompt_placeholder:
    st.markdown("**Chat** - _presiona Enter para enviar_")
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