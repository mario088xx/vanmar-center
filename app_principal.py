import streamlit as st

# --- CONFIGURACIÓN DE IDENTIDAD ---
CLIENT_ID = "98293623725-oaj0p863lnqkiuhoafv619st5gm57fsk.apps.googleusercontent.com"
REDIRECT_URI = "https://vanmar-center.streamlit.app"

st.set_page_config(page_title="VANMAR PRO", layout="centered")

# --- ESTILO VISUAL ---
st.markdown("""
    <style>
    .main-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(12px);
        border-radius: 20px;
        padding: 25px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        text-align: center;
        color: white;
    }
    .privacy-scroll {
        background: rgba(0, 0, 0, 0.3);
        padding: 15px;
        border-radius: 10px;
        text-align: left;
        font-size: 0.9rem;
        height: 150px;
        overflow-y: scroll;
        margin: 15px 0;
        border: 1px solid #444;
    }
    </style>
""", unsafe_allow_html=True)

if 'paso' not in st.session_state:
    st.session_state.paso = 'inicio'

# --- PANTALLA 1: ACCESO Y SLOGAN ---
if st.session_state.paso == 'inicio':
    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    st.title("VANMAR PRO")
    st.subheader("Gestión profesional de trámites vehiculares")
    st.write("---")
    
    # Botón de Google Real
    login_url = f"https://accounts.google.com/o/oauth2/auth?client_id={CLIENT_ID}&response_type=code&scope=openid%20email%20profile&redirect_uri={REDIRECT_URI}&prompt=select_account"
    
    st.markdown(f'''
        <a href="{login_url}" target="_self" style="text-decoration:none;">
            <div style="background-color: white; color: black; padding: 15px; border-radius: 10px; font-weight: bold; border: 1px solid #4285F4; margin-bottom: 20px;">
                Continuar con Google 🌐
            </div>
        </a>
    ''', unsafe_allow_html=True)
    
    if st.button("Registro Manual / Otros Correos"):
        st.session_state.paso = 'privacidad'
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# --- PANTALLA 2: DOCUMENTO Y PALOMITA (PRIVACIDAD) ---
elif st.session_state.paso == 'privacidad':
    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    st.subheader("📄 Aviso de Privacidad")
    
    st.markdown("""
    <div class="privacy-scroll">
        <b>Protocolo de Confidencialidad VANMAR:</b><br>
        1. Los datos vehiculares y personales son tratados con estricta privacidad.<br>
        2. El acceso está restringido únicamente a personal autorizado.<br>
        3. No se comparten bases de datos con entidades externas sin consentimiento.<br>
        4. Su información está protegida por encriptación de grado bancario.
    </div>
    """, unsafe_allow_html=True)
    
    aceptar = st.checkbox("He leído y acepto los términos de privacidad")
    
    if st.button("Siguiente"):
        if aceptar:
            st.session_state.paso = 'registro_manual'
            st.rerun()
        else:
            st.error("Por favor, marca la 'palomita' para continuar.")
    st.markdown('</div>', unsafe_allow_html=True)

# --- PANTALLA 3: FORMULARIO MANUAL ---
elif st.session_state.paso == 'registro_manual':
    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    st.subheader("Registro de Usuario")
    correo = st.text_input("Correo electrónico")
    tel = st.text_input("Teléfono de contacto (10 dígitos)")
    
    if st.button("Finalizar Registro"):
        if "@" in correo and len(tel) >= 10:
            st.session_state.paso = 'exito'
            st.rerun()
        else:
            st.warning("Verifique que el correo y el teléfono sean correctos.")
    st.markdown('</div>', unsafe_allow_html=True)

# --- PANTALLA 4: ÉXITO Y FRASE MOTIVADORA ---
elif st.session_state.paso == 'exito':
    st.balloons()
    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    st.success("### ¡Acceso Autorizado!")
    st.write("---")
    
    # AQUÍ TU FRASE MOTIVADORA COMO FORMA DE VIDA
    st.markdown("""
    ### 💡 Frase del Día:
    "El éxito no es solo llegar al destino, sino la precisión y la integridad con la que recorres cada trámite del camino."
    
    **Tu propósito VANMAR hoy:**
    * ⛽ Gestiona con la máxima potencia.
    * 🎗️ Protege la privacidad de cada expediente.
    * 🍎 Mantén la disciplina como bandera.
    * **Agradece a Dios por la oportunidad de servir con excelencia en cada gestión vehicular.**
    """)
    st.markdown('</div>', unsafe_allow_html=True)
