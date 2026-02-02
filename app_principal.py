import streamlit as st

# --- CONFIGURACIÓN DE IDENTIDAD ---
CLIENT_ID = "98293623725-oaj0p863lnqkiuhoafv619st5gm57fsk.apps.googleusercontent.com"
REDIRECT_URI = "https://vanmar-center.streamlit.app/"

st.set_page_config(page_title="VANMAR PRO", layout="centered")

# --- DISEÑO EDITORIAL CON RESPLANDOR AZUL SOBRIO ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Inter:wght@300;400;600&display=swap');
    
    .stApp {
        background-color: #050505;
        color: #E0E0E0;
        font-family: 'Inter', sans-serif;
    }
    
    /* Tarjeta con desvanecimiento azul reservado */
    .editorial-card {
        background: #0a0a0a;
        border-radius: 30px;
        padding: 40px;
        margin: 20px 0;
        border: 1px solid rgba(66, 133, 244, 0.15);
        box-shadow: 0 0 40px rgba(66, 133, 244, 0.05); /* Resplandor muy sutil */
    }
    
    .title-vanmar { font-family: 'Playfair Display', serif; font-size: 3rem; color: white; margin-bottom: 0; }
    .subtitle-vanmar { text-transform: uppercase; letter-spacing: 4px; font-size: 0.75rem; color: #666; margin-bottom: 40px; }
    
    .btn-google {
        background: white;
        color: black;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
        font-weight: 600;
        letter-spacing: 1px;
        display: block;
        text-decoration: none;
        margin-bottom: 20px;
        transition: 0.3s;
    }
    
    .privacy-box {
        background: rgba(255, 255, 255, 0.03);
        padding: 20px;
        border-radius: 15px;
        font-size: 0.85rem;
        line-height: 1.6;
        color: #999;
        height: 150px;
        overflow-y: scroll;
        margin-bottom: 20px;
        border: 1px solid #222;
    }
    </style>
""", unsafe_allow_html=True)

if 'paso' not in st.session_state:
    st.session_state.paso = 'inicio'

# --- 1. PORTADA ---
if st.session_state.paso == 'inicio':
    st.markdown('<div class="editorial-card">', unsafe_allow_html=True)
    st.markdown('<h1 class="title-vanmar">VANMAR PRO</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle-vanmar">Gestión profesional de trámites vehiculares</p>', unsafe_allow_html=True)
    
    login_url = f"https://accounts.google.com/o/oauth2/auth?client_id={CLIENT_ID}&response_type=code&scope=openid%20email%20profile&redirect_uri={REDIRECT_URI}&prompt=select_account"
    
    st.markdown(f'<a href="{login_url}" target="_self" class="btn-google">CONTINUAR CON GOOGLE 🌐</a>', unsafe_allow_html=True)
    
    if st.button("REGÍSTRATE"):
        st.session_state.paso = 'privacidad'
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# --- 2. PRIVACIDAD (EL DOCUMENTO Y PALOMITA) ---
elif st.session_state.paso == 'privacidad':
    st.markdown('<div class="editorial-card">', unsafe_allow_html=True)
    st.markdown('<h2 style="font-family:Playfair Display; color:white;">Protocolo de Privacidad</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="privacy-box">
        <b>Compromiso de Confidencialidad VANMAR:</b><br>
        Este sistema protege la identidad de cada aliado y gestor bajo protocolos de encriptación 
        de alta seguridad. La información vehicular tratada en este portal es de uso exclusivo 
        para la gestión profesional y no será compartida con terceros sin previa autorización. 
        Su privacidad es la base de nuestra confianza mutua.
    </div>
    """, unsafe_allow_html=True)
    
    palomita = st.checkbox("Acepto los términos de confidencialidad")
    
    if st.button("SIGUIENTE"):
        if palomita:
            st.session_state.paso = 'registro_manual'
            st.rerun()
        else:
            st.error("Es obligatorio aceptar con la palomita para continuar.")
    st.markdown('</div>', unsafe_allow_html=True)

# --- 3. REGISTRO MANUAL ---
elif st.session_state.paso == 'registro_manual':
    st.markdown('<div class="editorial-card">', unsafe_allow_html=True)
    st.markdown('<h2 style="font-family:Playfair Display; color:white;">Identificación</h2>', unsafe_allow_html=True)
    email = st.text_input("Correo corporativo")
    whatsapp = st.text_input("WhatsApp (10 dígitos)")
    
    if st.button("ACTIVAR ACCESO"):
        if "@" in email and len(whatsapp) >= 10:
            st.session_state.paso = 'exito'
            st.rerun()

# --- 4. CIERRE CON FRASE MOTIVADORA ---
elif st.session_state.paso == 'exito':
    st.balloons()
    st.markdown('<div class="editorial-card">', unsafe_allow_html=True)
    st.markdown('<h1 class="title-vanmar" style="font-size:2rem;">ACCESO AUTORIZADO</h1>', unsafe_allow_html=True)
    
    st.markdown("""
    <div style="font-style: italic; border-top: 1px solid #333; border-bottom: 1px solid #333; padding: 25px 0; margin: 30px 0; text-align: center; color: white;">
        "El éxito no es solo llegar al destino, sino la precisión y la integridad con la que recorres cada trámite del camino."
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    **Propósito VANMAR:**
    * **Fuerza:** Ejecuta con la potencia de un motor de alto rendimiento.
    * **Lealtad:** La privacidad de tu equipo es la base de tu imperio.
    * **Gratitud:** Agradece a Dios por la visión de orden y excelencia que hoy lideras.
    """)
    st.markdown('</div>', unsafe_allow_html=True)
