import streamlit as st

# --- CONFIGURACIÓN ---
CLIENT_ID = "98293623725-oaj0p863lnqkiuhoafv619st5gm57fsk.apps.googleusercontent.com"
REDIRECT_URI = "https://vanmar-center.streamlit.app"

st.set_page_config(page_title="VANMAR PRO", layout="centered")

# --- ESTILO ---
st.markdown("""
    <style>
    .main-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(12px);
        border-radius: 20px;
        padding: 30px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        text-align: center;
        color: white;
    }
    .privacy-box {
        background: rgba(0, 0, 0, 0.2);
        padding: 15px;
        border-radius: 10px;
        text-align: left;
        font-size: 0.85rem;
        height: 150px;
        overflow-y: scroll;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

if 'paso' not in st.session_state:
    st.session_state.paso = 'login'

# --- 1. PANTALLA DE ACCESO ---
if st.session_state.paso == 'login':
    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    st.title("VANMAR PRO")
    st.write("Portal de Gestión y Operaciones")
    
    login_url = f"https://accounts.google.com/o/oauth2/auth?client_id={CLIENT_ID}&response_type=code&scope=openid%20email%20profile&redirect_uri={REDIRECT_URI}"
    st.markdown(f'<a href="{login_url}" target="_self" style="background-color: white; color: black; padding: 12px 24px; border-radius: 8px; text-decoration: none; font-weight: bold; display: block; margin: 20px 0;">Continuar con Google 🌐</a>', unsafe_allow_html=True)
    
    if st.button("Acceso Manual"):
        st.session_state.paso = 'privacidad'
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# --- 2. CARTA DE PRIVACIDAD (EL RESPALDO) ---
elif st.session_state.paso == 'privacidad':
    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    st.subheader("Aviso de Privacidad y Confidencialidad")
    
    st.markdown("""
    <div class="privacy-box">
        <b>1. Protección de Datos:</b> VANMAR PRO garantiza que la información recolectada (correo y contacto) se utilizará exclusivamente para fines operativos internos.<br><br>
        <b>2. Confidencialidad:</b> Las identidades de aliados, gestores y personal administrativo están protegidas bajo protocolos de acceso restringido.<br><br>
        <b>3. No Divulgación:</b> No compartimos bases de datos con terceros. Su número de contacto es utilizado únicamente para validación de identidad y notificaciones críticas del sistema.<br><br>
        <b>4. Derechos ARCO:</b> El usuario tiene derecho a solicitar la eliminación de sus datos en cualquier momento.
    </div>
    """, unsafe_allow_html=True)
    
    aceptar = st.checkbox("He leído y acepto los términos de privacidad")
    
    if st.button("Continuar"):
        if aceptar:
            st.session_state.paso = 'registro'
            st.rerun()
        else:
            st.warning("Debe aceptar los términos para continuar.")
    st.markdown('</div>', unsafe_allow_html=True)

# --- 3. REGISTRO DE CONTACTO ---
elif st.session_state.paso == 'registro':
    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    st.subheader("Vinculación de Perfil")
    st.write("Ingrese su número de contacto para recibir acceso al centro operativo.")
    
    telefono = st.text_input("Número de WhatsApp (10 dígitos)")
    
    if st.button("Activar Acceso"):
        if len(telefono) >= 10:
            st.session_state.paso = 'final'
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# --- 4. CIERRE CON FILOSOFÍA ---
elif st.session_state.paso == 'final':
    st.balloons()
    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    st.success("### Acceso Autorizado")
    st.write("Bienvenido a la red de VANMAR PRO.")
    st.write("---")
    st.markdown("""
    ### 🙏 Frase de Vida:
    "La productividad es el acto de dar sentido al tiempo, y la privacidad es el acto de dar valor a las personas."
    
    **Tu propósito hoy:**
    * ⛽ Ejecuta con precisión quirúrgica.
    * 🎗️ Protege la información de tu equipo.
    * 🍎 Mantén la visión clara en cada trámite.
    * **Agradece a Dios por la oportunidad de liderar con orden y respeto.**
    """)
    st.markdown('</div>', unsafe_allow_html=True)
