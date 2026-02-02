import streamlit as st

# --- CONFIGURACIÓN DE SEGURIDAD ---
CLIENT_ID = "98293623725-oaj0p863lnqkiuhoafv619st5gm57fsk.apps.googleusercontent.com"
REDIRECT_URI = "https://vanmar-center.streamlit.app"

st.set_page_config(page_title="VANMAR PRO", layout="centered")

# --- ESTILO CRISTAL (SIN NOMBRES EXPUESTOS) ---
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; }
    .main-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 30px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        text-align: center;
        color: white;
    }
    .google-btn {
        background-color: white;
        color: #1f2937;
        font-weight: bold;
        text-decoration: none;
        padding: 15px 25px;
        border-radius: 10px;
        display: inline-block;
        width: 100%;
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# --- LÓGICA DE NAVEGACIÓN ---
if 'paso' not in st.session_state:
    st.session_state.paso = 'inicio'

# PANTALLA 1: ACCESO SEGURO
if st.session_state.paso == 'inicio':
    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    st.markdown("<h1>VANMAR <span style='color:#4285F4'>PRO</span></h1>", unsafe_allow_html=True)
    st.write("Bienvenido al Portal de Gestión de Activos.")
    st.write("---")
    
    # URL REAL DE GOOGLE OAUTH
    login_url = f"https://accounts.google.com/o/oauth2/auth?client_id={CLIENT_ID}&response_type=code&scope=openid%20email%20profile&redirect_uri={REDIRECT_URI}"
    
    st.markdown(f'<a href="{login_url}" target="_self" class="google-btn">Continuar con Google 🌐</a>', unsafe_allow_html=True)
    
    st.write("O utiliza el acceso para aliados externos")
    if st.button("Registro Manual / Otros Correos"):
        st.session_state.paso = 'manual'
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# PANTALLA 2: REGISTRO MANUAL PRIVADO
elif st.session_state.paso == 'manual':
    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    st.subheader("Validación de Identidad")
    email = st.text_input("Correo electrónico corporativo o personal")
    password = st.text_input("Contraseña de acceso", type="password")
    
    if st.button("Solicitar Acceso"):
        if "@" in email:
            st.info("Se ha enviado una solicitud de validación a su correo.")
            st.session_state.paso = 'finalizado'
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# PANTALLA 3: CONFIRMACIÓN Y FILOSOFÍA
elif st.session_state.paso == 'finalizado':
    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    st.success("### Proceso Iniciado")
    st.write("Su identidad está siendo verificada por el protocolo de seguridad VANMAR.")
    st.write("---")
    st.markdown("""
    **Próximos pasos:**
    1. Recibirá un correo de confirmación.
    2. Deberá vincular su número de contacto privado.
    
    ### 🙏 Frase de Vida:
    "La excelencia es el resultado de cuidar lo que nadie ve, para lograr lo que todos admiran."
    """)
    st.markdown('</div>', unsafe_allow_html=True)
