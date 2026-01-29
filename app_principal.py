import streamlit as st

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(page_title="VANMAR PRO", page_icon="🚗", layout="centered")

# 2. DISEÑO OXFORD (CONTRASTE ALTO)
st.markdown("""
    <style>
    header {visibility: hidden;} footer {visibility: hidden;}
    .stApp { background-color: #121212; } /* Negro Grafito / Oxford */

    .main-box { 
        max-width: 400px; margin: auto; text-align: center; 
        padding: 20px; color: #FFFFFF;
    }

    .logo-circle {
        width: 100px; height: 100px; border: 2px solid #4285F4; border-radius: 50%;
        margin: 0 auto 20px; display: flex; align-items: center; justify-content: center;
        font-size: 32px; font-weight: bold; background-color: #1E1E1E;
    }

    .title-text { font-size: 28px; font-weight: 800; margin-bottom: 10px; color: #FFFFFF; }
    .pro-text { color: #4285F4; }
    
    .welcome-msg { font-size: 18px; color: #E0E0E0; margin-bottom: 30px; line-height: 1.4; }

    /* Botones Estilo Gmail */
    .stButton>button {
        width: 100%; border-radius: 8px; height: 50px; font-weight: 600;
        border: none; font-size: 16px; transition: 0.3s;
    }
    .btn-google button { background-color: #FFFFFF !important; color: #000000 !important; }
    .btn-main button { background-color: #4285F4 !important; color: #FFFFFF !important; }

    /* Inputs */
    .stTextInput>div>div>input {
        background-color: #1E1E1E !important; color: white !important;
        border: 1px solid #333 !important; border-radius: 8px !important;
    }
    label { color: #E0E0E0 !important; font-weight: 500 !important; }
    </style>
    """, unsafe_allow_html=True)

# GESTIÓN DE FLUJO
if 'auth' not in st.session_state: st.session_state.auth = False
if 'step' not in st.session_state: st.session_state.step = 'login'

# --- PANTALLA 1: LOGIN (ESTILO GMAIL/LANDING) ---
if st.session_state.step == 'login':
    st.markdown('<div class="main-box">', unsafe_allow_html=True)
    st.markdown('<div class="logo-circle">VM</div>', unsafe_allow_html=True)
    st.markdown('<div class="title-text">VANMAR <span class="pro-text">PRO</span></div>', unsafe_allow_html=True)
    st.markdown('<div class="welcome-msg">Gestión vehicular inteligente para expertos.</div>', unsafe_allow_html=True)

    # Simulación de validación
    st.markdown('<div class="btn-google">', unsafe_allow_html=True)
    if st.button("Continuar con Google"):
        st.info("⚠️ Conexión con Google API activa. Por favor ingresa tu correo abajo para validar.")
    st.markdown('</div>', unsafe_allow_html=True)

    st.write("---")
    user_email = st.text_input("Correo electrónico", placeholder="nombre@ejemplo.com")
    user_pass = st.text_input("Contraseña", type="password", placeholder="••••••••")

    st.markdown('<div class="btn-main" style="margin-top:20px;">', unsafe_allow_html=True)
    if st.button("Iniciar Sesión"):
        if "@" in user_email and len(user_pass) > 4:
            st.session_state.auth = True
            st.session_state.step = 'wa_config'
            st.rerun()
        else:
            st.error("Por favor, ingresa un correo y contraseña válidos.")
    st.markdown('</div></div>', unsafe_allow_html=True)

# --- PANTALLA 2: CONFIGURA TU WHATSAPP (CONTEXTUAL) ---
elif st.session_state.step == 'wa_config':
    st.markdown('<div class="main-box">', unsafe_allow_html=True)
    st.markdown("## 📲 Enlace de Seguridad")
    st.markdown("""
    <div style='text-align: left; background-color: #1E1E1E; padding: 20px; border-radius: 10px; border-left: 5px solid #4285F4;'>
    <b>¿Para qué necesitamos tu número?</b><br><br>
    • Notificaciones automáticas de tus citas.<br>
    • Reportes de tus aliados (como <b>Bigotes</b>).<br>
    • Alertas de seguridad de tu cuenta.
    </div>
    """, unsafe_allow_html=True)
    
    st.write("")
    cel = st.text_input("Número de celular de trabajo (10 dígitos)", placeholder="Ej: 5512345678")
    
    st.markdown('<div class="btn-main">', unsafe_allow_html=True)
    if st.button("Validar y Entrar al Sistema"):
        if len(cel) == 10:
            st.session_state.user_wa = cel
            st.session_state.step = 'main_menu'
            st.rerun()
        else:
            st.error("El número debe tener 10 dígitos.")
    st.markdown('</div></div>', unsafe_allow_html=True)

# --- PANTALLA 3: MENÚ DE TRABAJO (TUS ALIADOS) ---
elif st.session_state.step == 'main_menu':
    st.markdown(f"### 🚀 Panel Principal")
    st.markdown(f"Bienvenido. Registrando trámites para: **{st.session_state.user_wa}**")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("📝 TRÁMITE PROPIO"):
            st.session_state.tipo = "PROPIO"
            st.session_state.step = 'upload'
            st.rerun()
    with col2:
        if st.button("🤝 TRÁMITE ALIADO"):
            st.session_state.tipo = "ALIADO"
            st.session_state.step = 'upload'
            st.rerun()

# --- SIGUIENTES PASOS ---
elif st.session_state.step == 'upload':
    st.subheader(f"Carga de Expediente: {st.session_state.tipo}")
    if st.session_state.tipo == "ALIADO":
        # Aquí recordamos a Bigotes como aliado frecuente
        aliado = st.selectbox("Selecciona tu Aliado:", ["Bigotes", "Liz", "Emilio", "Otros"])
    
    st.file_uploader("Subir Cita / Documento Maestro", type=['pdf', 'jpg', 'png'])
    if st.button("Volver"):
        st.session_state.step = 'main_menu'
        st.rerun()
