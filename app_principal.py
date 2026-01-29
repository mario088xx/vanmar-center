import streamlit as st
import urllib.parse

# 1. CONFIGURACIÓN TÉCNICA
st.set_page_config(page_title="VANMAR PRO", page_icon="💎", layout="centered")

# 2. DISEÑO VISUAL (CSS) - FORZANDO EL LOOK DE TU IMAGEN
st.markdown("""
    <style>
    /* Ocultar elementos de Streamlit */
    header {visibility: hidden;}
    footer {visibility: hidden;}
    #MainMenu {visibility: hidden;}
    .stApp { background-color: #f5f5f7; }

    /* Contenedor tipo iPhone para Laptop y Celular */
    .iphone-container {
        background-color: #1a2a40; /* Azul petróleo de la imagen */
        border-radius: 40px;
        max-width: 360px;
        margin: auto;
        overflow: hidden;
        color: white;
        font-family: 'Helvetica Neue', sans-serif;
        box-shadow: 0 20px 40px rgba(0,0,0,0.3);
        border: 4px solid #333;
    }
    
    .top-part { padding: 40px 20px; text-align: center; }
    .bottom-part { 
        background-color: white; 
        padding: 30px 25px; 
        border-radius: 35px 35px 0 0; 
        color: #333;
    }

    .logo-box {
        width: 70px; height: 70px;
        border: 2px solid white; border-radius: 50%;
        margin: 0 auto 15px; display: flex;
        align-items: center; justify-content: center; font-size: 24px; font-weight: bold;
    }

    .icon-grid { display: flex; justify-content: space-around; margin-bottom: 25px; }
    .icon-unit { text-align: center; font-size: 10px; color: #86868b; }
    .circle-bg { 
        width: 42px; height: 42px; border-radius: 50%; 
        background: #f0f0f5; display: flex; align-items: center; 
        justify-content: center; font-size: 20px; margin-bottom: 5px;
    }

    /* Estilo Botones Apple */
    .stButton>button {
        border-radius: 12px; height: 48px; font-weight: 600;
        border: none; width: 100%;
    }
    .stButton>button:first-child { background-color: #4285F4 !important; color: white !important; }
    
    /* Quitar espacios extra de Streamlit */
    .block-container { padding-top: 2rem; }
    </style>
    """, unsafe_allow_html=True)

# --- LÓGICA DE NAVEGACIÓN ---
if 'step' not in st.session_state:
    st.session_state.step = 'login'

# --- PANTALLA 1: LOGIN IDENTICO A TU IMAGEN ---
if st.session_state.step == 'login':
    # El contenedor visual
    st.markdown('<div class="iphone-container">', unsafe_allow_html=True)
    
    # Parte Azul (Logo y Bienvenida)
    st.markdown(f"""
        <div class="top-part">
            <div class="logo-box">VM</div>
            <h2 style='margin:0; color:white;'>VANMAR <span style='color:#4285F4;'>PRO</span></h2>
            <p style='font-size:18px; font-weight:bold; margin-top:15px; color:white;'>Bienvenido a tu gestión vehicular profesional.</p>
            <p style='font-size:11px; opacity:0.8; color:white;'>Regístrate para continuar</p>
        </div>
        <div class="bottom-part">
            <div class="icon-grid">
                <div class="icon-unit"><div class="circle-bg">🚗</div>Trámites</div>
                <div class="icon-unit"><div class="circle-bg">📄</div>Documentos</div>
                <div class="icon-unit"><div class="circle-bg">✅</div>Control</div>
            </div>
    """, unsafe_allow_html=True)
    
    # Botón Google (simulado con botón de Streamlit)
    if st.button("Continue with Google 🌐"):
        st.session_state.step = 'wa_config'
        st.rerun()
        
    st.markdown("<p style='text-align:center; color:#888; margin:10px 0; font-size:12px;'>— o —</p>", unsafe_allow_html=True)
    
    # Inputs compactos
    email = st.text_input("Email", placeholder="you@example.com", label_visibility="collapsed")
    password = st.text_input("Password", type="password", placeholder="••••••••", label_visibility="collapsed")
    
    if st.button("Sign in"):
        if email and password:
            st.session_state.step = 'wa_config'
            st.rerun()
    
    st.markdown("""
            <p style='text-align:center; font-size:11px; margin-top:15px; color:#4285F4;'>
                Forgot password? &nbsp;&nbsp;&nbsp; Need an account? Sign up
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- PANTALLA 2: REGISTRO WHATSAPP ---
elif st.session_state.step == 'wa_config':
    st.markdown("<h2 style='text-align:center;'>📲 Configura tu WhatsApp</h2>", unsafe_allow_html=True)
    st.write("Registra tu número de trabajo para recibir las notificaciones diarias de tus citas.")
    num = st.text_input("Número (10 dígitos)", placeholder="Ej: 5512345678")
    if st.button("Activar Sistema"):
        if len(num) == 10:
            st.session_state.user_wa = "52" + num
            st.session_state.step = 'main'
            st.rerun()
        else:
            st.error("Por favor ingresa 10 dígitos.")

# --- PANTALLA 3: FLUJO PRINCIPAL ---
elif st.session_state.step == 'main':
    st.title("🚀 Panel de Trabajo")
    st.write(f"Bienvenido. Sistema listo para operar con el WhatsApp: {st.session_state.user_wa}")
    if st.button("Cerrar Sesión"):
        st.session_state.step = 'login'
        st.rerun()
