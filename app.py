import streamlit as st

st.set_page_config(page_title="UIEPCh", page_icon="🤖", layout="centered")

st.logo("images/logoUich.png")

st.html("""
  <style>
    img[data-testid="stSidebarLogo"] {
        width: 7.75rem;
        height: 3.2rem;
        margin-top: 1.5em;
        max-height: none !important;
        max-width: none !important;
    }    
  </style>
""")

page_chat = st.Page("chat.py", title="Asistente Virtual", icon="💬", default=True)
page_info = st.Page("info.py", title="Acerca de UICh", icon="🏫")

pg = st.navigation(
    [page_chat,page_info]
)

pg.run()
