import streamlit as st

# --- CONFIGURACIÓN DE IDENTIDAD ---
CLIENT_ID = "98293623725-oaj0p863lnqkiuhoafv619st5gm57fsk.apps.googleusercontent.com"
REDIRECT_URI = "https://vanmar-center.streamlit.app/"

st.set_page_config(page_title="VANMAR PRO", layout="centered")

# --- CSS: ESTÉTICA MINIMALISTA Y LUJO DISCRETO ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@200;400;600&display=swap');
    
    .stApp {
        background: radial-gradient(circle at center, #1e293b 0%, #0f172a 100%);
        color: #f8fafc;
        font-family: 'Inter', sans-serif;
    }
    
    .main-title {
        font-size: 3.5rem;
        font-weight: 200;
        letter-spacing: -2px;
        text-align: center;
        color: #e2e8f0;
        margin-bottom: 0px;
    }
    
    .sub-title {
        text-transform: uppercase;
        letter-spacing: 5px;
        font-size: 0.7rem;
        color: #94a3b8;
        text-align: center;
        margin-bottom: 60px;
    }

    /* Botón Google: Efecto Glassmorphism sutil */
    .google-btn {
        display: block;
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        color: white;
        text-align: center;
        padding: 18px;
        border-radius: 50px;
        text-decoration: none;
        font-weight: 400;
        letter-spacing: 1px;
        font-size: 0.85rem;
        transition: all 0.3s ease;
        margin-bottom: 15px;
    }
    .google-btn:hover {
        background: rgba(255, 255, 255, 0.1);
        border: 1px solid rgba(255, 255, 255, 0.3);
    }

    /* Estilo para el botón de registro manual */
    .stButton>button {
        background: transparent !important;
        color: #94a3b8 !important;
        border: 1px solid rgba(148, 163, 184, 0.3) !important;
        border-radius: 50px !important;
        width: 100% !important;
        font-weight: 200 !important;
        letter-spacing: 1px !important;
        text-transform: uppercase !important;
        font-size: 0.75rem !important;
    }
    
    .footer-tags {
        margin-top: 100px;
        text-align: center;
        font-size: 0.65rem;
        letter-spacing: 2px;
        color: #475569;
        text-transform: uppercase;
    }
    </style>
""", unsafe_allow_html=True)

if 'paso' not in st.session_state:
    st.session_state.paso = 'inicio'

# --- LAYOUT ---
col1, col2, col3 = st.columns([1, 4, 1])

with col2:
    if st.session_state.paso == 'inicio':
        st.markdown('<h1 class="main-title">VANMAR PRO</h1>', unsafe_allow_html=True)
        st.markdown('<p class="sub-title">Gestión profesional de trámites vehiculares</p>', unsafe_allow_html=True)
        
        # Botón Google Real
        login_url = f"https://accounts.google.com/o/oauth2/auth?client_id={CLIENT_ID}&response_type=code&scope=openid%20email%20profile&redirect_uri={REDIRECT_URI}&prompt=select_account"
        
        st.markdown(f'<a href="{login_url}" target="_self" class="google-btn">CONTINUAR CON GOOGLE</a>', unsafe_allow_html=True)
        
        if st.button("REGÍSTRATE"):
            st.session_state.paso = 'privacidad'
            st.rerun()
            
        st.markdown('<div class="footer-tags">GESTIÓN DE ÉLITE • CONFIDENCIALIDAD ABSOLUTA • VISIÓN ESTRATÉGICA</div>', unsafe_allow_html=True)

    elif st.session_state.paso == 'privacidad':
        st.markdown('<h2 style="font-weight:200; text-align:center;">Privacidad</h2>', unsafe_allow_html=True)
        st.write("---")
        st.markdown("""
        <div style="font-size:0.8rem; color:#94a3b8; line-height:1.6; text-align:justify;">
            VANMAR PRO opera bajo los más altos estándares de confidencialidad. Sus datos vehiculares y personales 
            están protegidos por encriptación avanzada.
        </div>
        """, unsafe_allow_html=True)
        
        aceptar = st.checkbox("Acepto los términos de confidencialidad")
        if st.button("SIGUIENTE"):
            if aceptar:
                st.session_state.paso = 'registro'
                st.rerun()

    elif st.session_state.paso == 'registro':
        st.markdown('<h2 style="font-weight:200; text-align:center;">Registro</h2>', unsafe_allow_html=True)
        correo = st.text_input("EMAIL")
        tel = st.text_input("WHATSAPP")
        if st.button("FINALIZAR"):
            if "@" in correo and len(tel) >= 10:
                st.session_state.paso = 'exito'
                st.rerun()

    elif st.session_state.paso == 'exito':
        st.markdown('<h1 class="main-title" style="font-size:2.5rem;">BIENVENIDO</h1>', unsafe_allow_html=True)
        st.markdown('<div class="footer-tags">ACCESO AUTORIZADO</div>', unsafe_allow_html=True)
        st.write("")
        # Aquí la frase aparece solo al final, como un cierre de éxito
        st.markdown("""
        <div style="text-align:center; font-style:italic; color:#94a3b8; border-top:1px solid #334155; padding-top:20px;">
            "El éxito no es solo llegar al destino, sino la precisión y la integridad con la que recorres cada trámite del camino."
        </div>
        """, unsafe_allow_html=True)
