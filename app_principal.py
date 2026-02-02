import streamlit as st

# --- CONFIGURACIÓN DE IDENTIDAD ---
CLIENT_ID = "98293623725-oaj0p863lnqkiuhoafv619st5gm57fsk.apps.googleusercontent.com"
REDIRECT_URI = "https://vanmar-center.streamlit.app/"

st.set_page_config(page_title="VANMAR PRO", layout="wide")

# --- CSS: ESTÉTICA DE DOCUMENTACIÓN DE LUJO ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@300;400&family=Inter:wght@200;400;700&display=swap');
    
    .stApp { background-color: #ffffff; color: #1a1a1a; font-family: 'Inter', sans-serif; }
    
    /* Líneas divisorias estéticas tipo planos arquitectónicos */
    .divider { height: 1px; background-color: #e5e5e5; margin: 40px 0; }
    
    .hero-title {
        font-family: 'Inter', sans-serif;
        font-weight: 700;
        font-size: 4rem;
        letter-spacing: -3px;
        color: #000;
        line-height: 0.9;
        margin-bottom: 10px;
    }
    
    .mono-text {
        font-family: 'IBM Plex Mono', monospace;
        text-transform: uppercase;
        font-size: 0.75rem;
        letter-spacing: 2px;
        color: #666;
    }
    
    /* Botones con estilo de terminal de lujo */
    .btn-main {
        display: block;
        border: 1px solid #000;
        background: #000;
        color: #fff;
        padding: 20px;
        text-align: center;
        text-decoration: none;
        font-weight: 500;
        letter-spacing: 1px;
        transition: 0.3s;
    }
    .btn-main:hover { background: #333; color: #fff; }
    
    .btn-secondary {
        display: block;
        border: 1px solid #e5e5e5;
        background: transparent;
        color: #000;
        padding: 15px;
        text-align: center;
        text-decoration: none;
        font-size: 0.8rem;
        margin-top: 10px;
    }
    </style>
""", unsafe_allow_html=True)

if 'paso' not in st.session_state:
    st.session_state.paso = 'portada'

# --- ESTRUCTURA ---
left_col, mid_col, right_col = st.columns([1, 2, 1])

with mid_col:
    if st.session_state.paso == 'portada':
        st.markdown('<p class="mono-text">SISTEMA DE GESTIÓN DE ACTIVOS / VER 2026.02</p>', unsafe_allow_html=True)
        st.markdown('<h1 class="hero-title">VANMAR<br>PRO.</h1>', unsafe_allow_html=True)
        st.markdown('<p style="font-size: 1.1rem; color: #444;">Gestión profesional de trámites vehiculares con rigor documental.</p>', unsafe_allow_html=True)
        
        st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
        
        login_url = f"https://accounts.google.com/o/oauth2/auth?client_id={CLIENT_ID}&response_type=code&scope=openid%20email%20profile&redirect_uri={REDIRECT_URI}&prompt=select_account"
        
        st.markdown(f'<a href="{login_url}" target="_self" class="btn-main">CONTINUAR CON GOOGLE</a>', unsafe_allow_html=True)
        
        if st.button("REGÍSTRATE (ACCESO MANUAL)"):
            st.session_state.paso = 'legal'
            st.rerun()

    elif st.session_state.paso == 'legal':
        st.markdown('<p class="mono-text">SECCIÓN 01 / PROTOCOLO</p>', unsafe_allow_html=True)
        st.markdown('<h2 style="font-weight:700; font-size:2.5rem; letter-spacing:-1px;">Privacidad.</h2>', unsafe_allow_html=True)
        
        st.markdown("""
        <div style="font-size:0.9rem; border-left: 2px solid #000; padding-left: 20px; color: #666; margin: 30px 0;">
            Toda la información contenida en esta plataforma está sujeta a la Ley Federal de Protección de Datos Personales. 
            VANMAR PRO garantiza la anonimización de identidades y la seguridad de cada expediente vehicular procesado.
        </div>
        """, unsafe_allow_html=True)
        
        aceptar = st.checkbox("ACEPTO EL COMPROMISO DE CONFIDENCIALIDAD")
        
        if st.button("CONFIRMAR Y SIGUIENTE"):
            if aceptar:
                st.session_state.paso = 'registro'
                st.rerun()

    elif st.session_state.paso == 'registro':
        st.markdown('<p class="mono-text">SECCIÓN 02 / IDENTIFICACIÓN</p>', unsafe_allow_html=True)
        st.markdown('<h2 style="font-weight:700; font-size:2.5rem; letter-spacing:-1px;">Credenciales.</h2>', unsafe_allow_html=True)
        correo = st.text_input("EMAIL")
        tel = st.text_input("WHATSAPP (10 DÍGITOS)")
        
        if st.button("ACTIVAR CUENTA"):
            if "@" in correo and len(tel) >= 10:
                st.session_state.paso = 'final'
                st.rerun()

    elif st.session_state.paso == 'final':
        st.markdown('<p class="mono-text">ESTADO: ACCESO AUTORIZADO</p>', unsafe_allow_html=True)
        st.markdown('<h1 class="hero-title">ÉXITO.</h1>', unsafe_allow_html=True)
        
        st.markdown("""
        <div style="margin: 40px 0; padding: 30px; border: 1px solid #000; text-align: center;">
            <p style="font-family: 'IBM Plex Mono', monospace; font-size: 1.2rem; color: #000;">
                "El éxito no es solo llegar al destino, sino la precisión y la integridad con la que recorres cada trámite del camino."
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <p style="text-align: center; font-size: 0.8rem; color: #888;">
            <b>POTENCIA • PRIVACIDAD • DISCIPLINA</b><br>
            Agradece a Dios por la visión de orden y excelencia que hoy lideras.
        </p>
        """, unsafe_allow_html=True)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
