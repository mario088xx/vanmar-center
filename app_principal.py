import streamlit as st

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(page_title="VANMAR PRO", page_icon="🚗", layout="centered")

# 2. DISEÑO PROFESIONAL CON BACKGROUND DE AUTOS
st.markdown("""
    <style>
    header {visibility: hidden;} footer {visibility: hidden;}
    
    /* Fondo con patrón sutil de autos */
    .stApp {
        background-color: #121212;
        background-image: url("https://www.transparenttextures.com/patterns/carbon-fibre.png");
    }

    .main-box { 
        max-width: 400px; margin: auto; text-align: center; 
        padding: 30px; color: #FFFFFF;
        background: rgba(30, 30, 30, 0.9);
        border-radius: 20px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    }

    .logo-circle {
        width: 80px; height: 80px; border: 2px solid #4285F4; border-radius: 50%;
        margin: 0 auto 20px; display: flex; align-items: center; justify-content: center;
        background-color: #FFFFFF; font-size: 40px;
    }

    .title-text { font-size: 28px; font-weight: 800; color: #FFFFFF; }
    .pro-text { color: #4285F4; }
    .welcome-msg { font-size: 16px; color: #BBB; margin-bottom: 25px; }

    /* Botones Limpios */
    .stButton>button {
        width: 100%; border-radius: 10px; height: 50px; font-weight: 600;
        border: none; cursor: pointer;
    }
    .btn-google button { background-color: #FFFFFF !important; color: #444 !important; border: 1px solid #ddd !important; }
    .btn-main button { background-color: #4285F4 !important; color: white !important; }

    /* Estilo de inputs */
    .stTextInput>div>div>input {
        background-color: #252525 !important; color: white !important;
        border: 1px solid #444 !important; border-radius: 8px !important;
    }
    </style>
    """, unsafe_allow_html=True)

# GESTIÓN DE PASOS
if 'step' not in st.session_state: st.session_state.step = 'login'

# --- PANTALLA 1: LOGIN (ESTILO GOOGLE/GMAIL) ---
if st.session_state.step == 'login':
    st.markdown('<div class="main-box">', unsafe_allow_html=True)
    st.markdown('<div class="logo-circle">🚗</div>', unsafe_allow_html=True) # Icono de auto
    st.markdown('<div class="title-text">VANMAR <span class="pro-text">PRO</span></div>', unsafe_allow_html=True)
    st.markdown('<div class="welcome-msg">Gestión de Trámites Vehiculares Profesional</div>', unsafe_allow_html=True)

    # Botón Google (Acceso Directo)
    st.markdown('<div class="btn-google">', unsafe_allow_html=True)
    if st.button("Continuar con Google 🌐"):
        # En la versión final, aquí se conecta con el selector de cuentas de Google
        st.session_state.user = "Usuario Google"
        st.session_state.step = 'wa_config'
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

    st.write("o")

    # Registro Manual
    email = st.text_input("Correo electrónico")
    password = st.text_input("Contraseña", type="password")

    st.markdown('<div class="btn-main" style="margin-top:10px;">', unsafe_allow_html=True)
    if st.button("Iniciar Sesión"):
        if email and password:
            st.session_state.user = email
            st.session_state.step = 'wa_config'
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("<p style='font-size:12px; margin-top:15px; color:#4285F4;'>¿No tienes cuenta? Regístrate aquí</p>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# --- PANTALLA 2: WHATSAPP (EL POR QUÉ) ---
elif st.session_state.step == 'wa_config':
    st.markdown('<div class="main-box">', unsafe_allow_html=True)
    st.markdown("### 📲 Enlace de Notificaciones")
    st.write("Para enviarte las alertas de tus citas y reportes de aliados como Bigotes, vincula tu número de trabajo.")
    
    cel = st.text_input("WhatsApp (10 dígitos)", placeholder="5512345678")
    
    st.markdown('<div class="btn-main">', unsafe_allow_html=True)
    if st.button("Activar y Continuar"):
        if len(cel) == 10:
            st.session_state.wa = cel
            st.session_state.step = 'menu'
            st.rerun()
    st.markdown('</div></div>', unsafe_allow_html=True)

# --- PANTALLA 3: MENÚ (TUS ALIADOS) ---
elif st.session_state.step == 'menu':
    st.markdown(f"### 🚀 ¿Qué haremos hoy?")
    st.write(f"Sesión activa: {st.session_state.wa}")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("TRÁMITE PROPIO"):
            st.session_state.origen = "PROPIO"
            st.session_state.step = 'carga'
            st.rerun()
    with col2:
        if st.button("ALIADOS"):
            st.session_state.origen = "ALIADOS"
            st.session_state.step = 'carga'
            st.rerun()

# --- PANTALLA 4: CARGA Y FRASE FINAL ---
elif st.session_state.step == 'carga':
    st.subheader(f"Registro: {st.session_state.origen}")
    if st.session_state.origen == "ALIADOS":
        aliado = st.selectbox("¿De quién es el trámite?", ["Bigotes", "Liz", "Emilio", "Otros"])
    
    st.file_uploader("Subir Cita (Documento Maestro)")
    
    if st.button("Finalizar"):
        st.success("Trámite guardado.")
        # REGRESA LA FRASE MOTIVACIONAL
        st.markdown("""
        ---
        ### 🙏 ¡Éxito en tu camino!
        Recuerda:
        * ⛽ Gasolina revisada.
        * 🎗️ Cinturón puesto.
        * 🍎 Desayuno listo.
        * **Agradece a Dios por este nuevo día.**
        """)
        if st.button("Nuevo Registro"):
            st.session_state.step = 'menu'
            st.rerun()
