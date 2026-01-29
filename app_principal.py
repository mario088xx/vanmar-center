import streamlit as st
import urllib.parse

# 1. CONFIGURACIÓN DE PÁGINA (Limpia y profesional)
st.set_page_config(page_title="VANMAR PRO", page_icon="💎", layout="centered")

# 2. CSS PARA COPIAR TU IMAGEN AL 100%
st.markdown("""
    <style>
    /* Ocultar elementos de Streamlit */
    header {visibility: hidden;}
    footer {visibility: hidden;}
    #MainMenu {visibility: hidden;}
    .stApp { background-color: #f5f5f7; }

    /* Contenedor tipo iPhone Centrado */
    .main-container {
        background-color: #1a2a40; /* El azul oscuro de tu imagen */
        border-radius: 40px;
        padding: 0;
        margin: auto;
        max-width: 380px;
        overflow: hidden;
        color: white;
        font-family: 'Helvetica Neue', sans-serif;
        box-shadow: 0 20px 40px rgba(0,0,0,0.3);
    }
    
    .top-section { padding: 40px 20px; text-align: center; }
    .bottom-section { 
        background-color: white; 
        padding: 30px 25px; 
        border-radius: 40px 40px 0 0; 
        color: #333;
    }

    .logo-circle {
        width: 80px; height: 80px;
        border: 2px solid white; border-radius: 50%;
        margin: 0 auto 15px; display: flex;
        align-items: center; justify-content: center; font-weight: bold;
    }

    .icon-row { display: flex; justify-content: space-around; margin-bottom: 25px; }
    .icon-box { text-align: center; font-size: 10px; color: #86868b; }
    .icon-circle { 
        width: 45px; height: 45px; border-radius: 50%; 
        background: #f0f0f5; display: flex; align-items: center; 
        justify-content: center; font-size: 20px; margin-bottom: 5px;
    }

    /* Estilo de Botones */
    .stButton>button {
        border-radius: 12px; height: 50px; font-weight: 600;
        border: none; transition: 0.3s;
    }
    .google-btn button { background-color: #4285F4 !important; color: white !important; }
    .signin-btn button { background-color: #4285F4 !important; color: white !important; }
    
    /* Inputs */
    .stTextInput>div>div>input { border-radius: 10px; background-color: #f5f5f7; border: 1px solid #ddd; }
    </style>
    """, unsafe_allow_html=True)

# --- LÓGICA DE NAVEGACIÓN ---
if 'step' not in st.session_state:
    st.session_state.step = 'login'

# --- PANTALLA 1: LOGIN IDENTICO A TU IMAGEN ---
if st.session_state.step == 'login':
    # Usamos columnas para centrar la "App" en la laptop
    izq, centro, der = st.columns([1, 2, 1])
    
    with centro:
        st.markdown(f"""
        <div class="main-container">
            <div class="top-section">
                <div class="logo-circle">VM</div>
                <h2 style='margin:0;'>VANMAR <span style='color:#4285F4;'>PRO</span></h2>
                <p style='font-size:18px; font-weight:bold; margin-top:20px;'>Bienvenido a tu gestión vehicular profesional.</p>
                <p style='font-size:12px; opacity:0.8;'>Regístrate para continuar</p>
            </div>
            <div class="bottom-section">
                <div class="icon-row">
                    <div class="icon-box"><div class="icon-circle">🚗</div>Trámites</div>
                    <div class="icon-box"><div class="icon-circle">📄</div>Documentos</div>
                    <div class="icon-box"><div class="icon-circle">✅</div>Control</div>
                </div>
        """, unsafe_allow_html=True)
        
        # Botón Google
        st.markdown('<div class="google-btn">', unsafe_allow_html=True)
        if st.button("Continue with Google 🌐"):
            st.session_state.step = 'wa_config'
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown("<p style='text-align:center; color:#888; margin:10px 0;'>— o —</p>", unsafe_allow_html=True)
        
        # Inputs compactos
        email = st.text_input("Email", placeholder="you@example.com", label_visibility="collapsed")
        password = st.text_input("Password", type="password", placeholder="••••••••", label_visibility="collapsed")
        
        st.markdown('<div class="signin-btn">', unsafe_allow_html=True)
        if st.button("Sign in"):
            if email and password:
                st.session_state.step = 'wa_config'
                st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown("""
            <p style='text-align:center; font-size:12px; margin-top:15px; color:#4285F4;'>
                Forgot password? &nbsp;&nbsp;&nbsp; Need an account? Sign up
            </p>
            </div>
        </div>
        """, unsafe_allow_html=True)

# --- PANTALLA 2: REGISTRO WHATSAPP ---
elif st.session_state.step == 'wa_config':
    st.markdown("<h2 style='text-align:center;'>📲 Casi listo</h2>", unsafe_allow_html=True)
    st.write("Registra tu WhatsApp para recibir las alertas de Bigotes y tus otros aliados.")
    num = st.text_input("Número de 10 dígitos")
    if st.button("Activar VANMAR PRO"):
        if len(num) == 10:
            st.session_state.user_wa = "52" + num
            st.session_state.step = 'main'
            st.rerun()

# --- PANTALLA 3: FLUJO DE CARGA (PROPIO/ALIADOS) ---
elif st.session_state.step == 'main':
    st.title("🚀 Iniciar Trámite")
    # Aquí sigue el flujo de cargar cita, elegir ALIADOS (Bigotes, etc.)
    if st.button("Regresar al Login (Prueba)"):
        st.session_state.step = 'login'
        st.rerun()
