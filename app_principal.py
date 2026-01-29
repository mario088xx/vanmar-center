import streamlit as st

# 1. CONFIGURACIÓN
st.set_page_config(page_title="VANMAR PRO", page_icon="🚗", layout="centered")

# 2. CSS PROFESIONAL (Glassmorphism & Oxford)
st.markdown("""
    <style>
    header {visibility: hidden;} footer {visibility: hidden;}
    .stApp {
        background-color: #0F172A; /* Oxford Blue Profundo */
        background-image: radial-gradient(circle at center, #1E293B 0%, #0F172A 100%);
    }

    /* Tarjeta Principal con Transparencia */
    .main-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        border-radius: 24px;
        padding: 40px 20px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        text-align: center;
        max-width: 400px;
        margin: auto;
    }

    /* Icono de Auto Premium */
    .premium-logo {
        font-size: 50px;
        margin-bottom: 10px;
        filter: drop-shadow(0 0 10px #4285F4);
    }

    .title-text { font-size: 28px; font-weight: 800; color: white; margin-bottom: 5px; }
    .pro-tag { color: #4285F4; }
    .tagline { color: #94A3B8; font-size: 14px; margin-bottom: 30px; }

    /* Fila de Iconos que se habían perdido */
    .status-row { display: flex; justify-content: space-around; margin-bottom: 35px; }
    .status-unit { text-align: center; color: #94A3B8; font-size: 11px; }
    .circle-icon { 
        width: 45px; height: 45px; border-radius: 50%; 
        background: rgba(66, 133, 244, 0.1); border: 1px solid rgba(66, 133, 244, 0.3);
        display: flex; align-items: center; justify-content: center; 
        font-size: 20px; margin: 0 auto 8px; color: white;
    }

    /* Botones Estilo Google Original */
    .stButton>button {
        width: 100%; border-radius: 10px; height: 50px; font-weight: 600; border: none;
    }
    .google-btn button { 
        background-color: white !important; color: #1F2937 !important; 
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .login-btn button { background-color: #4285F4 !important; color: white !important; margin-top: 10px; }

    /* Inputs */
    .stTextInput>div>div>input {
        background-color: rgba(0,0,0,0.2) !important; color: white !important;
        border: 1px solid #334155 !important; border-radius: 10px !important;
    }
    </style>
    """, unsafe_allow_html=True)

# NAVEGACIÓN
if 'step' not in st.session_state: st.session_state.step = 'login'

# --- PANTALLA 1: LOGIN (CALCADO PROFESIONAL) ---
if st.session_state.step == 'login':
    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    st.markdown('<div class="premium-logo">🏎️</div>', unsafe_allow_html=True) # Icono estilizado
    st.markdown('<div class="title-text">VANMAR <span class="pro-tag">PRO</span></div>', unsafe_allow_html=True)
    st.markdown('<div class="tagline">Gestión de Trámites Vehiculares Profesional</div>', unsafe_allow_html=True)

    # LOS ICONOS QUE SE PERDÍAN
    st.markdown("""
        <div class="status-row">
            <div class="status-unit"><div class="circle-icon">🚗</div>Trámites</div>
            <div class="status-unit"><div class="circle-icon">📄</div>Documentos</div>
            <div class="status-unit"><div class="circle-icon">✅</div>Control</div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="google-btn">', unsafe_allow_html=True)
    if st.button("Continuar con Google 🌐"):
        # AQUÍ ES DONDE SE CONECTARÁ EL POP-UP REAL
        st.session_state.step = 'wa_config'
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("<p style='color:#64748B; margin:15px 0;'>— o ingresa manualmente —</p>", unsafe_allow_html=True)

    email = st.text_input("Correo electrónico", placeholder="ejemplo@gmail.com")
    password = st.text_input("Contraseña", type="password")

    st.markdown('<div class="login-btn">', unsafe_allow_html=True)
    if st.button("Iniciar Sesión"):
        if email and password:
            st.session_state.step = 'wa_config'
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("<p style='font-size:12px; margin-top:20px; color:#4285F4;'>¿Eres nuevo? <b>Regístrate aquí</b></p>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# --- PANTALLA 2: WHATSAPP (POST-LOGIN) ---
elif st.session_state.step == 'wa_config':
    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    st.markdown("### 📲 Casi listo")
    st.write("Vincula tu número de WhatsApp para recibir alertas de tus aliados (como **Bigotes**) y el estatus de tus trámites.")
    cel = st.text_input("WhatsApp a 10 dígitos")
    if st.button("Activar Sistema"):
        if len(cel) == 10:
            st.session_state.step = 'menu'
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# --- SIGUIENTE FLUJO ---
elif st.session_state.step == 'menu':
    st.title("🚀 Panel Operativo")
    st.write("Bienvenido al centro de mando.")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("TRÁMITE PROPIO"): st.info("Abriendo carga...")
    with col2:
        if st.button("ALIADOS"): st.info("Seleccionando aliado...")
