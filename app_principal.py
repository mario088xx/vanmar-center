import streamlit as st

# --- CONFIGURACIÓN DE IDENTIDAD ---
CLIENT_ID = "98293623725-oaj0p863lnqkiuhoafv619st5gm57fsk.apps.googleusercontent.com"
REDIRECT_URI = "https://vanmar-center.streamlit.app/"

st.set_page_config(page_title="VANMAR PRO", layout="centered")

# --- CSS: LUJO DISCRETO Y BOTONES SIMÉTRICOS ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@100;300;400&display=swap');
    
    .stApp {
        background: radial-gradient(circle at center, #1e293b 0%, #080c14 100%);
        color: #f8fafc;
        font-family: 'Inter', sans-serif;
    }
    
    .logo-container { text-align: center; margin-bottom: 20px; color: #94a3b8; }
    
    .main-title {
        font-size: 3rem;
        font-weight: 100;
        letter-spacing: 4px;
        text-align: center;
        color: #ffffff;
        margin-bottom: 5px;
    }
    
    .sub-title {
        text-transform: uppercase;
        letter-spacing: 6px;
        font-size: 0.65rem;
        color: #64748b;
        text-align: center;
        margin-bottom: 50px;
    }

    /* Contenedor de botones para que sean iguales */
    .btn-box {
        max-width: 320px;
        margin: 0 auto;
    }

    .action-btn {
        display: block;
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        color: white;
        text-align: center;
        padding: 15px 0;
        border-radius: 4px;
        text-decoration: none;
        font-weight: 300;
        letter-spacing: 2px;
        font-size: 0.75rem;
        transition: 0.3s;
        margin-bottom: 12px;
        width: 100%;
        text-transform: uppercase;
    }
    
    .action-btn:hover {
        background: rgba(255, 255, 255, 0.08);
        border: 1px solid rgba(255, 255, 255, 0.4);
    }

    /* Ajuste para el botón de Streamlit */
    .stButton>button {
        background: rgba(255, 255, 255, 0.03) !important;
        color: white !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 4px !important;
        height: 50px !important;
        width: 100% !important;
        font-weight: 300 !important;
        letter-spacing: 2px !important;
        font-size: 0.75rem !important;
        text-transform: uppercase !important;
    }
    </style>
""", unsafe_allow_html=True)

if 'paso' not in st.session_state:
    st.session_state.paso = 'inicio'

# --- PANTALLA DE INICIO ---
if st.session_state.paso == 'inicio':
    # Logo minimalista de auto (Icono SVG sutil)
    st.markdown("""
        <div class="logo-container">
            <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1" stroke-linecap="round" stroke-linejoin="round">
                <rect x="1" y="10" width="22" height="8" rx="2"></rect>
                <path d="M7 10l2.4-4.6A2 2 0 0 1 11.2 4h1.6a2 2 0 0 1 1.8 1.4L17 10"></path>
                <circle cx="7" cy="18" r="2"></circle>
                <circle cx="17" cy="18" r="2"></circle>
            </svg>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<h1 class="main-title">VANMAR PRO</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">Gestión profesional de trámites vehiculares</p>', unsafe_allow_html=True)
    
    st.markdown('<div class="btn-box">', unsafe_allow_html=True)
    
    # Botón Google
    login_url = f"https://accounts.google.com/o/oauth2/auth?client_id={CLIENT_ID}&response_type=code&scope=openid%20email%20profile&redirect_uri={REDIRECT_URI}&prompt=select_account"
    st.markdown(f'<a href="{login_url}" target="_self" class="action-btn">Continuar con Google</a>', unsafe_allow_html=True)
    
    # Botón Registro
    if st.button("Regístrate"):
        st.session_state.paso = 'privacidad'
        st.rerun()
        
    st.markdown('</div>', unsafe_allow_html=True)

# --- FLUJO POSTERIOR (PRIVACIDAD / EXITO) ---
elif st.session_state.paso == 'privacidad':
    st.markdown('<h3 style="text-align:center; font-weight:100;">PRIVACIDAD</h3>', unsafe_allow_html=True)
    st.markdown('<div style="font-size:0.7rem; color:#64748b; padding:20px; text-align:justify;">Toda gestión en VANMAR PRO está protegida por protocolos de confidencialidad absoluta.</div>', unsafe_allow_html=True)
    if st.checkbox("Acepto los términos"):
        if st.button("SIGUIENTE"):
            st.session_state.paso = 'exito'
            st.rerun()

elif st.session_state.paso == 'exito':
    st.markdown('<h1 class="main-title">BIENVENIDO</h1>', unsafe_allow_html=True)
    st.markdown("""
        <div style="text-align:center; font-size:0.8rem; color:#94a3b8; border-top:1px solid #1e293b; padding-top:20px; margin-top:40px;">
            "El éxito no es solo llegar al destino, sino la precisión e integridad con la que recorres cada trámite del camino."
        </div>
    """, unsafe_allow_html=True)
