import streamlit as st

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(page_title="VANMAR PRO", page_icon="🚗", layout="centered")

# 2. ESTILO OXFORD PREMIUM (Legibilidad 100%)
st.markdown("""
    <style>
    header {visibility: hidden;} footer {visibility: hidden;}
    .stApp { background-color: #0F172A; }
    .main-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(15px);
        border-radius: 28px;
        padding: 40px 25px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        text-align: center;
        max-width: 400px;
        margin: auto;
    }
    .premium-logo { font-size: 55px; margin-bottom: 15px; filter: drop-shadow(0 0 15px #4285F4); }
    .title-text { font-size: 30px; font-weight: 800; color: white; }
    .pro-tag { color: #4285F4; }
    .tagline { color: #94A3B8; font-size: 14px; margin-bottom: 30px; }
    
    /* Iconos con transparencia recuperados */
    .icon-box { 
        width: 50px; height: 50px; border-radius: 50%; 
        background: rgba(66, 133, 244, 0.15); border: 1px solid rgba(66, 133, 244, 0.4);
        display: flex; align-items: center; justify-content: center; font-size: 22px; margin: 0 auto 10px;
    }

    /* Botones Estilo Google */
    .stButton>button { width: 100%; border-radius: 12px; height: 52px; font-weight: 600; border: none; }
    .google-btn button { background-color: white !important; color: #1F2937 !important; box-shadow: 0 4px 12px rgba(0,0,0,0.2); }
    .login-btn button { background-color: #4285F4 !important; color: white !important; }
    </style>
    """, unsafe_allow_html=True)

# GESTIÓN DE ESTADOS
if 'logged_in' not in st.session_state: st.session_state.logged_in = False
if 'step' not in st.session_state: st.session_state.step = 'login'

# --- PANTALLA 1: LOGIN REALISTA ---
if st.session_state.step == 'login':
    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    st.markdown('<div class="premium-logo">🏎️</div>', unsafe_allow_html=True)
    st.markdown('<div class="title-text">VANMAR <span class="pro-tag">PRO</span></div>', unsafe_allow_html=True)
    st.markdown('<div class="tagline">Gestión de Trámites Vehiculares Profesional</div>', unsafe_allow_html=True)

    # Iconos de estatus (Trámites, Documentos, Control)
    col1, col2, col3 = st.columns(3)
    with col1: st.markdown('<div class="icon-box">🚗</div><small style="color:#94A3B8">Trámites</small>', unsafe_allow_html=True)
    with col2: st.markdown('<div class="icon-box">📄</div><small style="color:#94A3B8">Documentos</small>', unsafe_allow_html=True)
    with col3: st.markdown('<div class="icon-box">✅</div><small style="color:#94A3B8">Control</small>', unsafe_allow_html=True)

    st.write("---")
    
    st.markdown('<div class="google-btn">', unsafe_allow_html=True)
    if st.button("Continuar con Google 🌐"):
        # NOTA: Para que abra la ventanita de Google, necesitamos el Client ID. 
        # Por ahora simulamos la entrada exitosa de Mario.
        st.session_state.user_name = "Mario" 
        st.session_state.logged_in = True
        st.session_state.step = 'wa_config'
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("<p style='color:#64748B; margin:15px 0;'>o accede con tu cuenta</p>", unsafe_allow_html=True)
    email = st.text_input("Correo electrónico", placeholder="ejemplo@gmail.com")
    password = st.text_input("Contraseña", type="password")
    
    if st.button("Iniciar Sesión"):
        if email and password:
            st.session_state.user_name = email.split('@')[0]
            st.session_state.logged_in = True
            st.session_state.step = 'wa_config'
            st.rerun()

# --- PANTALLA 2: WHATSAPP (SOLO SI YA INICIÓ SESIÓN) ---
elif st.session_state.step == 'wa_config':
    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    st.markdown(f"### 👋 ¡Hola, {st.session_state.user_name}!")
    st.write("Para habilitar las notificaciones de tus trámites y reportes de aliados, vincula tu WhatsApp.")
    cel = st.text_input("Número a 10 dígitos", placeholder="55 1234 5678")
    if st.button("Activar e ir al Panel"):
        if len(cel) == 10:
            st.session_state.wa = cel
            st.session_state.step = 'menu'
            st.rerun()

# --- PANTALLA 3: MENÚ ALIADOS CON AUTOCOMPLETADO ---
elif st.session_state.step == 'menu':
    st.title("🚀 Panel de Control")
    tipo = st.radio("Selecciona Origen:", ["PROPIO", "ALIADOS"])
    
    if tipo == "ALIADOS":
        # LISTA SUGERIDA (Pero permite escribir manual)
        aliados_sugeridos = ["Bigotes", "Liz", "Emilio", "Pascual", "Raquel"]
        # El widget 'selectbox' con capacidad de búsqueda o un 'text_input' con sugerencias
        aliado = st.text_input("Nombre del Aliado / Gestor:", 
                              help="Escribe el nombre. Si ya existe, el sistema lo reconocerá.",
                              placeholder="Ej: Bigotes")
        if aliado in aliados_sugeridos:
            st.caption(f"✅ Aliado frecuente detectado: {aliado}")
    
    st.file_uploader("Subir Cita (Documento Maestro)")
    
    if st.button("Finalizar"):
        st.success("¡Registro completado!")
        st.markdown("""
            ---
            ### 🙏 ¡Éxito en tu jornada!
            * ⛽ Gasolina revisada.
            * 🎗️ Cinturón puesto.
            * 🍎 Desayuno listo.
            * **Agradece a Dios por este día.**
        """)
