import streamlit as st

# --- CONFIGURACIÓN DE IDENTIDAD ---
CLIENT_ID = "98293623725-oaj0p863lnqkiuhoafv619st5gm57fsk.apps.googleusercontent.com"
# Usamos la dirección EXACTA de tu configuración en Google Cloud
REDIRECT_URI = "https://vanmar-center.streamlit.app/"

st.set_page_config(page_title="VANMAR PRO", layout="centered")

# --- ESTILO EDITORIAL PREMIUM ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Inter:wght@300;400;600&display=swap');
    
    .stApp { background-color: #050505; color: #E0E0E0; font-family: 'Inter', sans-serif; }
    
    .title-vanmar { font-family: 'Playfair Display', serif; font-size: 3.5rem; color: white; text-align: center; margin-bottom: 0px; }
    .subtitle-vanmar { text-transform: uppercase; letter-spacing: 3px; font-size: 0.8rem; color: #888; text-align: center; margin-bottom: 40px; }
    
    .editorial-card {
        border-left: 1px solid #333;
        padding: 20px 0 20px 30px;
        margin: 20px 0;
    }
    
    .privacy-box {
        background: #111;
        padding: 20px;
        border: 1px solid #222;
        font-size: 0.85rem;
        line-height: 1.6;
        color: #bbb;
        height: 150px;
        overflow-y: scroll;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

if 'paso' not in st.session_state:
    st.session_state.paso = 'inicio'

# --- PANTALLA 1: PORTADA Y ACCESO ---
if st.session_state.paso == 'inicio':
    st.markdown('<h1 class="title-vanmar">VANMAR PRO</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle-vanmar">Gestión profesional de trámites vehiculares</p>', unsafe_allow_html=True)
    
    st.markdown('<div class="editorial-card">', unsafe_allow_html=True)
    
    # Botón de Google con dirección blindada
    login_url = f"https://accounts.google.com/o/oauth2/auth?client_id={CLIENT_ID}&response_type=code&scope=openid%20email%20profile&redirect_uri={REDIRECT_URI}&prompt=select_account"
    
    st.markdown(f'''
        <a href="{login_url}" target="_self" style="text-decoration:none;">
            <div style="border: 1px solid white; color: white; padding: 15px; text-align: center; font-weight: 600; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 20px;">
                Acceso vía Google Cloud 🌐
            </div>
        </a>
    ''', unsafe_allow_html=True)
    
    if st.button("REGISTRO MANUAL / OTROS CORREOS"):
        st.session_state.paso = 'privacidad'
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# --- PANTALLA 2: DOCUMENTO Y PALOMITA ---
elif st.session_state.paso == 'privacidad':
    st.markdown('<h2 style="font-family:Playfair Display; color:white;">Protocolo de Privacidad</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="privacy-box">
        <b>Compromiso de Confidencialidad:</b><br>
        En VANMAR PRO, la protección de datos es nuestra prioridad. Toda información vehicular, 
        identidad de gestores y aliados está resguardada bajo protocolos de cifrado avanzado. 
        Al continuar, usted acepta que sus datos serán utilizados estrictamente para fines 
        operativos y de seguridad interna de la plataforma.
    </div>
    """, unsafe_allow_html=True)
    
    palomita = st.checkbox("Acepto los términos de confidencialidad")
    
    if st.button("CONTINUAR"):
        if palomita:
            st.session_state.paso = 'registro_manual'
            st.rerun()
        else:
            st.error("Es obligatorio marcar la palomita de privacidad.")

# --- PANTALLA 3: REGISTRO MANUAL ---
elif st.session_state.paso == 'registro_manual':
    st.markdown('<h2 style="font-family:Playfair Display; color:white;">Identificación de Usuario</h2>', unsafe_allow_html=True)
    correo = st.text_input("Correo electrónico")
    whatsapp = st.text_input("WhatsApp (10 dígitos)")
    
    if st.button("VERIFICAR Y ENTRAR"):
        if "@" in correo and len(whatsapp) >= 10:
            st.session_state.paso = 'exito'
            st.rerun()
        else:
            st.warning("Por favor complete los datos correctamente.")

# --- PANTALLA 4: ÉXITO Y FRASE MOTIVADORA ---
elif st.session_state.paso == 'exito':
    st.balloons()
    st.markdown('<h1 class="title-vanmar" style="font-size:2.5rem;">ACCESO AUTORIZADO</h1>', unsafe_allow_html=True)
    st.write("---")
    
    st.markdown("""
    <div style="font-style: italic; border-top: 1px solid #333; border-bottom: 1px solid #333; padding: 20px 0; margin: 30px 0; text-align: center; color: white;">
        "El éxito no es solo llegar al destino, sino la precisión y la integridad con la que recorres cada trámite del camino."
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    **Tu propósito VANMAR hoy:**
    * ⛽ **Potencia:** Ejecuta cada gestión con la fuerza de un líder.
    * 🎗️ **Lealtad:** La privacidad de tus aliados es tu mayor valor.
    * 🍎 **Disciplina:** El orden es la clave del crecimiento.
    * **Agradece a Dios por permitirte liderar un sistema basado en la excelencia y el respeto.**
    """)
