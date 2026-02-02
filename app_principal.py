import streamlit as st

# --- CONFIGURACIÓN DE IDENTIDAD ---
CLIENT_ID = "98293623725-oaj0p863lnqkiuhoafv619st5gm57fsk.apps.googleusercontent.com"
REDIRECT_URI = "https://vanmar-center.streamlit.app/"

st.set_page_config(page_title="VANMAR PRO", layout="centered")

# --- DISEÑO EDITORIAL SUPREMO ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Bodoni+Moda:ital,wght@0,400;0,700;1,400&family=Montserrat:wght@300;400;600&display=swap');
    
    /* Fondo Editorial: Degradado de Negro Carbón a Gris Oxford */
    .stApp {
        background: radial-gradient(circle at top, #1c1c1c 0%, #000000 100%);
        color: #d4d4d4;
        font-family: 'Montserrat', sans-serif;
    }
    
    /* Título con estilo de cabecera de revista */
    .editorial-header {
        font-family: 'Bodoni Moda', serif;
        font-size: 4.5rem;
        color: #ffffff;
        text-align: center;
        margin-bottom: 0px;
        letter-spacing: -3px;
        line-height: 1;
    }
    
    .editorial-subtitle {
        font-family: 'Montserrat', sans-serif;
        text-transform: uppercase;
        letter-spacing: 6px;
        font-size: 0.7rem;
        color: #8a8a8a;
        text-align: center;
        margin-bottom: 60px;
        font-weight: 300;
    }
    
    /* Contenedor Minimalista */
    .editorial-content {
        max-width: 500px;
        margin: 0 auto;
        padding: 40px;
        border-top: 1px solid rgba(255,255,255,0.1);
    }
    
    /* Botón Continuar con Google - Estética Editorial */
    .btn-google {
        display: block;
        background-color: #ffffff;
        color: #000000;
        text-align: center;
        padding: 18px;
        text-decoration: none;
        font-weight: 600;
        letter-spacing: 2px;
        text-transform: uppercase;
        font-size: 0.8rem;
        transition: 0.4s;
        margin-bottom: 20px;
    }
    
    .btn-google:hover {
        background-color: #d4d4d4;
    }

    /* Frase Motivadora - Estilo Cita de Revista */
    .quote-box {
        font-family: 'Bodoni Moda', serif;
        font-style: italic;
        font-size: 1.4rem;
        color: #ffffff;
        text-align: center;
        line-height: 1.5;
        padding: 40px 20px;
        border-top: 1px solid #333;
        border-bottom: 1px solid #333;
        margin-top: 50px;
    }
    </style>
""", unsafe_allow_html=True)

if 'paso' not in st.session_state:
    st.session_state.paso = 'inicio'

# --- PANTALLA 1: PORTADA ---
if st.session_state.paso == 'inicio':
    st.markdown('<h1 class="editorial-header">VANMAR</h1>', unsafe_allow_html=True)
    st.markdown('<p class="editorial-subtitle">Gestión profesional de trámites vehiculares</p>', unsafe_allow_html=True)
    
    st.markdown('<div class="editorial-content">', unsafe_allow_html=True)
    
    login_url = f"https://accounts.google.com/o/oauth2/auth?client_id={CLIENT_ID}&response_type=code&scope=openid%20email%20profile&redirect_uri={REDIRECT_URI}&prompt=select_account"
    
    st.markdown(f'<a href="{login_url}" target="_self" class="btn-google">Continuar con Google</a>', unsafe_allow_html=True)
    
    if st.button("REGÍSTRATE"):
        st.session_state.paso = 'privacidad'
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# --- PANTALLA 2: PRIVACIDAD ---
elif st.session_state.paso == 'privacidad':
    st.markdown('<h2 style="font-family:Bodoni Moda; color:white; text-align:center;">Privacidad & Rigor</h2>', unsafe_allow_html=True)
    st.markdown('<p style="font-size:0.9rem; color:#8a8a8a; text-align:center; margin-bottom:30px;">DOCUMENTO DE CONFIDENCIALIDAD</p>', unsafe_allow_html=True)
    
    st.markdown("""
    <div style="background:#0a0a0a; padding:30px; border:1px solid #222; font-size:0.8rem; line-height:1.8; color:#888;">
        Toda gestión dentro de <b>VANMAR PRO</b> está blindada bajo protocolos de cifrado asimétrico. 
        La identidad de nuestros aliados es tratada con estricta reserva, garantizando que 
        la información vehicular sea utilizada únicamente para fines operativos.
    </div>
    """, unsafe_allow_html=True)
    
    aceptar = st.checkbox("ACEPTO EL COMPROMISO DE PRIVACIDAD")
    
    if st.button("SIGUIENTE"):
        if aceptar:
            st.session_state.paso = 'registro'
            st.rerun()

# --- PANTALLA 3: REGISTRO ---
elif st.session_state.paso == 'registro':
    st.markdown('<h2 style="font-family:Bodoni Moda; color:white; text-align:center;">Identificación</h2>', unsafe_allow_html=True)
    correo = st.text_input("CORREO ELECTRÓNICO")
    tel = st.text_input("WHATSAPP")
    
    if st.button("ACTIVAR ACCESO"):
        if "@" in correo and len(tel) >= 10:
            st.session_state.paso = 'exito'
            st.rerun()

# --- PANTALLA 4: ÉXITO ---
elif st.session_state.paso == 'exito':
    st.markdown('<h1 class="editorial-header" style="font-size:3rem;">BIENVENIDO</h1>', unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class="quote-box">
        "El éxito no es solo llegar al destino, sino la precisión y la integridad con la que recorres cada trámite del camino."
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="text-align:center; color:#8a8a8a; font-size:0.8rem; letter-spacing:1px;">
        GESTIÓN POTENTE • PRIVACIDAD TOTAL • DISCIPLINA DIARIA
        <br><br>
        <b>Agradece a Dios por la visión de orden y excelencia que hoy lideras.</b>
    </div>
    """, unsafe_allow_html=True)
