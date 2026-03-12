import streamlit as st

st.set_page_config(page_title="UIEPCh", page_icon="🤖", layout="centered")

st.logo("images/logoUich.png")

st.html("""
  <style>
    img[data-testid="stSidebarLogo"] {
        width: 7rem;
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

footer_html = """
<style>
.footer {
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
    background-color: white;
    color: black;
    text-align: center;
    padding: 5px;
}
</style>
<div class="footer">
    <p style= 'font-size: 0.8rem; padding-top: 7px;'>Copyright © 2026 | UICh | Todos los Derechos Reservados</p>
</div>
"""

st.markdown(footer_html, unsafe_allow_html=True)