import streamlit as st
import os
from dataclasses import dataclass
from typing import Literal

# Importaciones de LangChain
from langchain_chroma import Chroma
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_classic.chains.conversational_retrieval.base import ConversationalRetrievalChain
from langchain_classic.chains.conversation.memory import ConversationSummaryMemory


# Constantes
# Nombre de la carpeta donde se guardará la base de datos vectorial
PERSIST_DIRECTORY = "./chroma_db"
# Nombre del archivo pdf
PDF_PATH = "fichauich.pdf"

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
    
    if st.session_state.conversation and human_prompt:
        # Ejecutar la cadena con la pregunta del usuario
        # Nota: ConversationalRetrievalChain espera un diccionario con "question"
        with st.spinner("🦅 UIChito esta buscando en los documentos..."):
            response = st.session_state.conversation.invoke({"question": human_prompt})
            llm_response = response['answer']

        st.session_state.history.append(
            Message("human", human_prompt)
        )

        st.session_state.history.append(
            Message("ai", llm_response)
        )

#botones de sugerencia
def enviar_sugerencia(pregunta):
    """Procesa la pregunta cuando el usuario hace clic en un botón de sugerencia"""
    if st.session_state.conversation:
        # Ejecutar la cadena con la pregunta del botón
        with st.spinner("🦅 UIChito esta buscando en los documentos..."):
            response = st.session_state.conversation.invoke({"question": pregunta})
            llm_response = response['answer']

        # Guardar en el historial
        st.session_state.history.append(Message("human", pregunta))
        st.session_state.history.append(Message("ai", llm_response))

        st.rerun()

# Ejecución Principal
load_css()
initialize_session_state()

# Interfaz Principal

st.markdown("<h1 style='text-align: left; font-size: 4em; margin-bottom: 0; padding-bottom: 0;'>Hola, Futuro halcón</h1>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: left; font-size: 1.3em; margin-bottom: 0; padding-bottom: 0.3rem;'>¿En qué puedo ayudarte hoy?</h1>", unsafe_allow_html=True)

chat_placeholder = st.container()
prompt_placeholder = st.form("chat-form", clear_on_submit=True)

with chat_placeholder:
    for chat in st.session_state.history:
            
        div = f"""
        <div class="chat-row {'' if chat.origin == 'ai' else 'row-reverse'}">
            <div class="chat-icon" style="font-size:32px">
                {'🦅' if chat.origin == 'ai' else '👨🏻‍💻'}
            </div>
            <div class="chat-bubble {'ai-bubble' if chat.origin == 'ai' else 'human-bubble'}">
                    &#8203;{chat.message}                </div>
            </div>
        """
        st.markdown(div, unsafe_allow_html=True)

    for _ in range(3):
        st.markdown("")

#Construccion de botones
st.markdown("<p style='text-align: center; font-size: 0.9em; color: gray; margin-bottom: 1rem;'>💡 Puedes preguntarme cosas como:</p>", unsafe_allow_html=True)

# Creamos 3 columnas para los 3 botones
col_sug1, col_sug2, col_sug3 = st.columns(3)

# Botón 1
with col_sug1:
    if st.button("¿Cuáles son los papeles que necesito para inscribirme?", use_container_width=True):
        enviar_sugerencia("¿Cuáles son los papeles que necesito para inscribirme?")

# Botón 2
with col_sug2:
    if st.button("¿Qué carreras ofrece la universidad?", use_container_width=True):
        enviar_sugerencia("¿Qué carreras ofrece la universidad?")

# Botón 3
with col_sug3:
    if st.button("¿Cuál es el proceso de admisión?", use_container_width=True):
        enviar_sugerencia("¿Cuál es el proceso de admisión?")

st.markdown("<br>", unsafe_allow_html=True) # Un pequeño salto de línea para separar los botones del formulario

with prompt_placeholder:
    st.markdown("_Presiona Enter para enviar_")
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