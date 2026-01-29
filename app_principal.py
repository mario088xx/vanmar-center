import streamlit as st

# CONFIGURACIÓN DE PÁGINA
st.set_page_config(page_title="VANMAR PRO", page_icon="💎", layout="centered")

# CSS: CALCADO DE LA IMAGEN PROFESIONAL
st.markdown("""
    <style>
    header {visibility: hidden;} footer {visibility: hidden;} #MainMenu {visibility: hidden;}
    .stApp { background-color: white; }
    .main-box { max-width: 400px; margin: auto; text-align: center; font-family: sans-serif; padding: 10px; }
    .logo-circle {
        width: 90px; height: 90px; border: 3px solid #1a2a40; border-radius: 50%;
        margin: 0 auto 15px; display: flex; align-items: center; justify-content: center;
        font-size: 28px; font-weight: bold; color: #1a2a40;
    }
    .title-text { font-size: 24px; font-weight: 800; color: #1a2a40; }
    .pro-text { color: #4285F4; }
    .welcome-msg { font-size: 19px; font-weight: 600; color: #333; margin: 10px 0; }
    .icon-row { display: flex; justify-content: space-around; margin: 25px 0; }
    .icon-circle { 
        width: 48px; height: 48px; border-radius: 50%; background: #f0f0f5; 
        display: flex; align-items: center; justify-content: center; font-size: 20px; margin: 0 auto 5px;
    }
    .stButton>button { width: 100%; border-radius: 12px; height: 48px; font-weight: 600; border: none; }
    .btn-blue button { background-color: #4285F4 !important; color: white !important; }
    </style>
    """, unsafe_allow_html=True)

# GESTIÓN DE PASOS (STATE)
if 'step' not in st.session_state: st.session_state.step = 'login'

# --- PANTALLA 1: LOGIN (IDÉNTICO A IMAGEN) ---
if st.session_state.step == 'login':
    st.markdown('<div class="main-box">', unsafe_allow_html=True)
    st.markdown('<div class="logo-circle">VM</div>', unsafe_allow_html=True)
    st.markdown('<div class="title-text">VANMAR <span class="pro-text">PRO</span></div>', unsafe_allow_html=True)
    st.markdown('<div class="welcome-msg">Bienvenido a tu gestión vehicular profesional.</div>', unsafe_allow_html=True)
    st.markdown('<p style="color:#86868b; font-size:13px;">Regístrate para continuar</p>', unsafe_allow_html=True)
    
    st.markdown('<div class="icon-row"><div><div class="icon-circle">🚗</div><small>Trámites</small></div><div><div class="icon-circle">📄</div><small>Documentos</small></div><div><div class="icon-circle">✅</div><small>Control</small></div></div>', unsafe_allow_html=True)

    st.markdown('<div class="btn-blue">', unsafe_allow_html=True)
    if st.button("Continue with Google"):
        st.session_state.step = 'registro_celular'
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<p style="color:#999; margin:10px 0;">o</p>', unsafe_allow_html=True)
    st.text_input("Email", placeholder="you@example.com", label_visibility="collapsed")
    st.text_input("Password", type="password", placeholder="Contraseña", label_visibility="collapsed")
    
    st.markdown('<div class="btn-blue" style="margin-top:15px;">', unsafe_allow_html=True)
    if st.button("Sign in"):
        st.session_state.step = 'registro_celular'
        st.rerun()
    st.markdown('</div></div>', unsafe_allow_html=True)

# --- PANTALLA 2: REGISTRO CELULAR (POST-LOGIN) ---
elif st.session_state.step == 'registro_celular':
    st.markdown('<div class="main-box">', unsafe_allow_html=True)
    st.image("https://cdn-icons-png.flaticon.com/512/124/124034.png", width=50) # Icono WA
    st.header("Configura tu WhatsApp")
    st.write("Es necesario registrar tu celular de Trabajo para enviarte las notificaciones diarias y el estado de tus trámites.")
    cel = st.text_input("Número a 10 dígitos", placeholder="5512345678")
    if st.button("Confirmar y Entrar"):
        if len(cel) == 10:
            st.session_state.user_wa = "52" + cel
            st.session_state.step = 'seleccion_tramite'
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# --- PANTALLA 3: PROPIO O ALIADOS ---
elif st.session_state.step == 'seleccion_tramite':
    st.markdown('<div class="main-box">', unsafe_allow_html=True)
    st.subheader("¿Qué tipo de trámite vas a registrar?")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("PROPIO"):
            st.session_state.origen = "PROPIO"
            st.session_state.step = 'carga_documentos'
            st.rerun()
    with col2:
        if st.button("ALIADOS"):
            st.session_state.origen = "ALIADOS"
            st.session_state.step = 'carga_documentos'
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# --- PANTALLA 4: CARGA Y ALIADOS ---
elif st.session_state.step == 'carga_documentos':
    st.title(f"Expediente: {st.session_state.origen}")
    
    if st.session_state.origen == "ALIADOS":
        aliados = ["BIGOTES", "LIZ", "EMILIO", "PASCUAL", "ADRI", "ALONZO", "RAQUEL", "ALBERTO", "VICTOR", "FELIX", "OTRO"]
        aliado_sel = st.selectbox("¿De qué aliado es el trámite?", aliados)
    
    st.file_uploader("1. Sube la Cita (Requerido)")
    st.file_uploader("2. Solicitud")
    st.file_uploader("3. INE / Identificación")
    st.file_uploader("4. Comprobante de Pago")
    
    if st.button("Siguiente Paso"):
        st.session_state.step = 'asignacion_final'
        st.rerun()

# --- PANTALLA 5: ASIGNACIÓN Y CIERRE ---
elif st.session_state.step == 'asignacion_final':
    st.subheader("Asignación de Trámite")
    responsable = st.radio("¿Quién concluye el trámite?", ["VAN", "MAR"])
    
    if st.button("Finalizar Registro"):
        st.balloons()
        st.success("¡Trámite registrado con éxito!")
        st.markdown(f"""
            ### 🙏 ¡Éxito en tu día!
            Recuerda antes de salir:
            * ⛽ Revisa gasolina.
            * 🎗️ Cinturón de seguridad.
            * 🍎 Desayuna bien.
            * **Agradece a Dios por un nuevo día.**
        """)
        if st.button("Registrar otro"):
            st.session_state.step = 'seleccion_tramite'
            st.rerun()
