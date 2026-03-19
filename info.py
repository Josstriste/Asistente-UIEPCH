import streamlit as st

st.markdown(
    "<h1 style='text-align: center; font-size: 4em; margin-bottom: 0.2em; padding-bottom: 0; color: #7A1C30;'>Acerca de</h1>", unsafe_allow_html=True
    )

st.image("images/fachadaUICh.png", )

st.markdown(
    "<p style='text-align: justify; font-size: 1.2em; margin-top: 1.2rem; padding-bottom: 0;'>Somos una Institución de Educación Superior que forma profesionales de calidad, con actitud científica, creativa, solidaria, con espíritu emprendedor e innovador, sensibles a la diversidad cultural y comprometidos con el respeto a la valoración de la diferentes culturas.</p>",
    unsafe_allow_html=True
    )

col1, col2 = st.columns(2, gap="small", vertical_alignment='center')
with col1:
    st.image("images/fachadaiz.png")
with col2:
    st.markdown(
    "<p style='text-align: justify; font-size: 1.2em; margin-top: 0.5rem; padding: 0;'>Formando profesionistas acorde a las demandas de la sociedad y desarrollando actividades académicas, de investigación, difusión y extensión universitaria, para beneficiar a la Región, el Estado y el País, con la razón de mejorar el desarrollo humano en los nuevos retos de nuestra era.</p>",
    unsafe_allow_html=True
    )

st.markdown("---")

col_mision, col_vision, col_valores = st.columns(3, gap="medium")

estilo_tarjeta = """
    background-color: #FFFFFF;
    border: 1px solid #E6E6E6;
    border-radius: 15px;
    padding: 20px;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.05);
    height: 100%;
"""

with col_mision:
    st.markdown(f"""
    <div style="{estilo_tarjeta}">
        <h3 style="text-align: center; color: #7A1C30; margin-top: 0;">🎯 Misión</h3>
        <p style="text-align: justify; color: #4A4A4A; font-size: 0.95em;">
            Somos una institución de nivel superior que forma profesionistas; creativos, emprendedores y competitivos, a través de  programas educativos pertinentes a la zona de influencia, con un diseño curricular tecnológico y humanista, además de docentes comprometidos con la excelencia académica, para integrar  egresados profesionales con vocación de servicio y valores; a los diferentes sectores de la sociedad.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col_vision:
    st.markdown(f"""
    <div style="{estilo_tarjeta}">
        <h3 style="text-align: center; color: #7A1C30; margin-top: 0;">👁️ Visión</h3>
        <p style="text-align: justify; color: #4A4A4A; font-size: 0.95em;">
            Ser una institución de educación superior que tenga reconocimiento regional, estatal y nacional, con programas educativos acreditados, aplicando tecnologías de la información y comunicación en el proceso enseñanza-aprendizaje, con enfoque sustentable y sostenible; impactando como agente promotor del desarrollo socioeconómico y cultural a través de la vinculación con los sectores de la sociedad.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col_valores:
    st.markdown(f"""
    <div style="{estilo_tarjeta}">
        <h3 style="text-align: center; color: #7A1C30; margin-top: 0;">⭐ Valores</h3>
        <ul style="color: #4A4A4A; font-size: 0.95em; padding-left: 20px;">
            <li style="margin-bottom: 8px;"><b>Solidaridad</b></li>
            <li style="margin-bottom: 8px;"><b>Responsabilidad</b></li>
            <li style="margin-bottom: 8px;"><b>Humildad</b></li>
            <li style="margin-bottom: 8px;"><b>Empatía</b></li>
            <li style="margin-bottom: 8px;"><b>Creatividad</b></li>
            <li style="margin-bottom: 8px;"><b>Respeto</b></li>
            <li style="margin-bottom: 8px;"><b>Lealtad</b></li>
            <li style="margin-bottom: 8px;"><b>Honestidad</b></li>
            <li style="margin-bottom: 8px;"><b>Ética</b></li>
            <li style="margin-bottom: 8px;"><b>Equidad</b></li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

st.markdown(
    "<h1 style='text-align: center; font-size: 2em; color: #7A1C30; font-style: italic;'>La educación es la semilla de la prosperidad, en la UICh la sembramos cada día</h1>", unsafe_allow_html=True
    )

st.markdown(
    "<p style='text-align: center; font-size: 1.2em; margin-top: 0.5rem; padding: 0;'>Contactanos en Facebook como <a style= 'text-decoration: none; color: #7A1C30;' href= ""https://www.facebook.com/UIChOficial"">@UIChOficial</a></p>",
    unsafe_allow_html=True
    )