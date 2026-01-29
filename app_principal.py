import streamlit as st

# CONFIGURACIÓN TÉCNICA
st.set_page_config(page_title="VANMAR PRO", page_icon="💎", layout="centered")

# CSS: CALCADO EXACTO DE LA IMAGEN (Fondo blanco, círculos, botones azules)
st.markdown("""
    <style>
    /* Limpieza de interfaz */
    header {visibility: hidden;} footer {visibility: hidden;} #MainMenu {visibility: hidden;}
    .stApp { background-color: white; }
    
    /* Contenedor tipo Móvil centrado */
    .main-box { 
        max-width: 380px; 
        margin: auto; 
        text-align: center; 
        font-family: 'Segoe UI', sans-serif; 
        padding: 10px;
    }

    /* Logo Circular VM */
    .logo-circle {
        width: 90px; height: 90px; 
        border: 3px solid #1a2a40; border-radius: 50%;
        margin: 0 auto 15px; display: flex; 
        align-items: center; justify-content: center;
        font-size: 30px; font-weight: bold; color: #1a2a40;
    }

    /* Texto de Título */
    .title-text { font-size: 26px; font-weight: 800; color: #1a2a40; }
    .pro-text { color: #4285F4; }
    .welcome-msg { 
        font-size: 20px; font-weight: 600; color: #333; 
        line-height: 1.2; margin: 15px 0 5px 0; 
    }
    .subtitle { color: #86868b; font-size: 14px; margin-bottom: 30px; }

    /* Fila de Iconos */
    .icon-row { display: flex; justify-content: space-around; margin: 30px 0; }
    .icon-unit { text-align: center; font-size: 11px; color: #666; font-weight: 500; }
    .icon-circle { 
        width: 50px; height: 50px; border-radius: 50%; 
        background: #f0f0f5; display: flex; align-items: center; 
        justify-content: center; font-size: 22px; margin: 0 auto 8px;
        border: 1px solid #e0e0e0;
    }

    /* Botones Estilo Apple/Google */
    .stButton>button { 
        width: 100%; border-radius: 12px; height: 52px; 
        font-weight: 600; font-size: 16px; border: none; 
    }
    .btn-google button { background-color: #4285F4 !important; color: white !important; margin-bottom: 10px; }
    .btn-signin button { background-color: #4285F4 !important; color: white !important; }
    
    /* Inputs Estilizados */
    .stTextInput>div>div>input {
        border-radius: 10px; background-color: #fff; border: 1px solid #ddd; height: 48px;
    }
    </style>
    """, unsafe_allow_html=True)

# GESTIÓN DE PASOS (STATE)
if 'step' not in st.session_state:
    st.session_state.step = 'login'

# --- 1. PANTALLA DE LOGIN (IDÉNTICA A LA IMAGEN) ---
if st.session_state.step == 'login':
    st.markdown('<div class="main-box">', unsafe_allow_html=True)
    
    st.markdown('<div class="logo-circle">VM</div>', unsafe_allow_html=True)
    st.markdown('<div class="title-text">VANMAR <span class="pro-text">PRO</span></div>', unsafe_allow_html=True)
    st.markdown('<div class="welcome-msg">Bienvenido a tu gestión vehicular profesional.</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Regístrate para continuar</div>', unsafe_allow_html=True)
    
    # Iconos decorativos
    st.markdown("""
        <div class="icon-row">
            <div class="icon-unit"><div class="icon-circle">🚗</div>Trámites</div>
            <div class="icon-unit"><div class="icon-circle">📄</div>Documentos</div>
            <div class="icon-unit"><div class="icon-circle">✅</div>Control</div>
        </div>
    """, unsafe_allow_html=True)

    # Botones de Login
    st.markdown('<div class="btn-google">', unsafe_allow_html=True)
    if st.button("Continue with Google"):
        st.session_state.step = 'registro_celular'
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<p style="color:#999; margin:15px 0;">o</p>', unsafe_allow_html=True)

    st.text_input("Email", placeholder="you@example.com", label_visibility="collapsed")
    st.text_input("Password", type="password", placeholder="Contraseña", label_visibility="collapsed")
    
    st.markdown('<div class="btn-signin" style="margin-top:20px;">', unsafe_allow_html=True)
    if st.button("Sign in"):
        st.session_state.step = 'registro_celular'
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("""
        <div style="margin-top:25px; font-size:13px;">
            <a href="#" style="color:#4285F4; text-decoration:none;">Forgot password?</a> &nbsp;&nbsp; 
            <span style="color:#888;">Need an account?</span> <a href="#" style="color:#4285F4; text-decoration:none;">Sign up</a>
        </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# --- 2. PANTALLA REGISTRO CELULAR (Post-Login) ---
elif st.session_state.step == 'registro_celular':
    st.markdown('<div class="main-box">', unsafe_allow_html=True)
    st.markdown("## 📲 Configura tu WhatsApp")
    st.info("Es necesario registrar tu celular de trabajo para enviarte las notificaciones diarias y el estado de tus trámites.")
    
    cel = st.text_input("Número a 10 dígitos", placeholder="Ej: 5512345678")
    
    if st.button("Confirmar y Entrar"):
        if len(cel) == 10:
            st.session_state.user_wa = "52" + cel
            st.session_state.step = 'seleccion_tipo'
            st.rerun()
        else:
            st.error("Por favor, ingresa los 10 dígitos de tu número.")
    st.markdown('</div>', unsafe_allow_html=True)

# --- 3. PANTALLA PROPIO O ALIADOS ---
elif st.session_state.step == 'seleccion_tipo':
    st.markdown('<div class="main-box">', unsafe_allow_html=True)
    st.subheader("¿Qué tipo de trámite vas a registrar?")
    st.write("Selecciona una opción para continuar")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("PROPIO"):
            st.session_state.origen = "PROPIO"
            st.session_state.step = 'carga_tramite'
            st.rerun()
    with col2:
        if st.button("ALIADOS"):
            st.session_state.origen = "ALIADOS"
            st.session_state.step = 'carga_tramite'
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# --- 4. PANTALLA CARGA DE DOCUMENTOS ---
elif st.session_state.step == 'carga_tramite':
    st.subheader(f"Gestión de Trámite: {st.session_state.origen}")
    
    if st.session_state.origen == "ALIADOS":
        aliado = st.selectbox("Selecciona al Aliado:", ["BIGOTES", "LIZ", "EMILIO", "PASCUAL", "ADRI", "ALONZO", "RAQUEL", "ALBERTO", "VICTOR", "OTRO"])
    
    st.write("---")
    st.file_uploader("📂 Subir Cita (Documento Maestro)", type=['pdf', 'jpg', 'png'])
    st.file_uploader("📄 Solicitud de Trámite")
    st.file_uploader("🪪 INE / ID")
    st.file_uploader("💰 Comprobante de Pago")
    
    if st.button("Validar Expediente"):
        st.session_state.step = 'finalizacion'
        st.rerun()

# --- 5. PANTALLA FINALIZACIÓN Y ASIGNACIÓN ---
elif st.session_state.step == 'finalizacion':
    st.success("¡Expediente validado correctamente!")
    
    st.subheader("Asignación Final")
    resp = st.radio("¿Quién concluye este trámite?", ["VAN", "MAR"])
    
    if st.button("Finalizar Registro y Notificar"):
        st.balloons()
        st.markdown(f"""
            ### 🙏 ¡Trámite Finalizado con éxito!
            **Recuerda antes de salir:**
            * ⛽ Revisa gasolina.
            * 🎗️ Cinturón de seguridad.
            * 🍎 Desayuna o come bien.
            * **Agradece a Dios por un nuevo día de éxito.**
        """)
        
        if st.button("Registrar otro trámite"):
            st.session_state.step = 'seleccion_tipo'
            st.rerun()
