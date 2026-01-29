import streamlit as st
import urllib.parse

# CONFIGURACIÓN PARA OCULTAR MENÚS DE STREAMLIT Y FORZAR DISEÑO
st.set_page_config(page_title="VANMAR PRO", page_icon="💎", layout="centered")

st.markdown("""
    <style>
    /* Forzar fondo claro y ocultar basura de Streamlit */
    .stApp { background-color: #F5F5F7; }
    header {visibility: hidden;}
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Contenedor Principal tipo Tarjeta Apple */
    .login-card {
        background-color: white;
        padding: 40px 30px;
        border-radius: 28px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.1);
        text-align: center;
        max-width: 400px;
        margin: auto;
    }
    
    .logo-text { font-size: 32px; font-weight: 800; color: #1d1d1f; margin-bottom: 5px; }
    .logo-pro { color: #007AFF; }
    .welcome-text { font-size: 22px; font-weight: 600; color: #1d1d1f; line-height: 1.2; }
    .subtitle { color: #86868b; font-size: 14px; margin-bottom: 30px; }
    
    /* Fila de Iconos */
    .icon-row {
        display: flex;
        justify-content: space-around;
        margin-bottom: 40px;
    }
    .icon-item { text-align: center; }
    .icon-emoji { font-size: 30px; margin-bottom: 5px; }
    .icon-text { font-size: 11px; color: #86868b; text-transform: uppercase; letter-spacing: 1px; }

    /* Botones Estilizados */
    .stButton>button {
        border-radius: 14px;
        height: 52px;
        font-weight: 600;
        font-size: 16px;
        border: none;
    }
    .google-btn button {
        background-color: #007AFF !important;
        color: white !important;
    }
    .sign-in-btn button {
        background-color: #007AFF !important;
        color: white !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- INICIO DEL DISEÑO ---
if 'step' not in st.session_state:
    st.session_state.step = 'login'

if st.session_state.step == 'login':
    # Crear la tarjeta blanca
    st.markdown('<div class="login-card">', unsafe_allow_html=True)
    
    # Logo y Títulos
    st.markdown('<div class="logo-text">VANMAR <span class="logo-pro">PRO</span></div>', unsafe_allow_html=True)
    st.markdown('<div class="welcome-text">Bienvenido a tu gestión vehicular profesional.</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Regístrate para continuar</div>', unsafe_allow_html=True)
    
    # Fila de Iconos alineada
    st.markdown("""
        <div class="icon-row">
            <div class="icon-item"><div class="icon-emoji">🚗</div><div class="icon-text">Trámites</div></div>
            <div class="icon-item"><div class="icon-emoji">📄</div><div class="icon-text">Documentos</div></div>
            <div class="icon-item"><div class="icon-emoji">✅</div><div class="icon-text">Control</div></div>
        </div>
    """, unsafe_allow_html=True)

    # Botón Google (Clase personalizada)
    st.markdown('<div class="google-btn">', unsafe_allow_html=True)
    if st.button("Continue with Google 🌐"):
        st.session_state.step = 'wa_config'
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<p style="color:#86868b; margin:20px 0;">— o —</p>', unsafe_allow_html=True)

    # Inputs de Email/Pass
    email = st.text_input("Email", placeholder="you@example.com", label_visibility="collapsed")
    password = st.text_input("Password", type="password", placeholder="••••••••", label_visibility="collapsed")
    
    st.markdown('<div class="sign-in-btn">', unsafe_allow_html=True)
    if st.button("Sign in"):
        if email and password:
            st.session_state.step = 'wa_config'
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<p style="font-size:13px; margin-top:20px;"><a href="#" style="color:#007AFF; text-decoration:none;">Forgot password?</a> &nbsp;&nbsp; <a href="#" style="color:#007AFF; text-decoration:none;">Need an account? Sign up</a></p>', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True) # Fin de la tarjeta

# --- EL RESTO DEL CÓDIGO SE MANTIENE IGUAL PARA EL WHATSAPP ---
elif st.session_state.step == 'wa_config':
    st.title("📲 Configura tu WhatsApp")
    num = st.text_input("Número de 10 dígitos")
    if st.button("Siguiente"):
        st.session_state.user_wa = "52" + num
        st.session_state.step = 'main'
        st.rerun()
