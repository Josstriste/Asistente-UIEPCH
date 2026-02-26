import streamlit as st

st.set_page_config(page_title="UIEPCh", page_icon="🤖", layout="centered")
st.logo("images/v2Logo.png", size='large')

page_chat = st.Page("chat.py", title="Asistente Virtual", icon="💬", default=True)
page_info = st.Page("info.py", title="Acerca de UICh", icon="🏫")

pg = st.navigation(
    [page_chat,page_info]

)

pg.run()