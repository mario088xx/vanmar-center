import streamlit as st

# --- CONFIGURACIÓN DE IDENTIDAD ---
CLIENT_ID = "98293623725-oaj0p863lnqkiuhoafv619st5gm57fsk.apps.googleusercontent.com"
REDIRECT_URI = "https://vanmar-center.streamlit.app"

st.set_page_config(page_title="VANMAR PRO | Editorial", layout="centered")

# --- DISEÑO EDITORIAL (CSS PERSONALIZADO) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Inter:wght@300;400;600&display=swap');
    
    .stApp { background-color: #050505; color: #E0E0E0; font-family: 'Inter', sans-serif; }
    
    .editorial-title {
        font-family: 'Playfair Display', serif;
        font-size: 3.5rem;
        letter-spacing: -2px;
        margin-bottom: 0px;
        color: white;
        text-align: center;
    }
    .editorial-subtitle {
        text-transform: uppercase;
        letter-spacing: 4px;
        font-size: 0.8rem;
        color: #888;
        text-align: center;
        margin-bottom: 40px;
    }
    .main-container {
        border-left: 1px solid #333;
        padding-left: 30px;
        margin-top: 50px;
    }
    .privacy-box {
        background: #111;
        padding: 20px;
        border: 1px solid #222;
        font-size: 0.9rem;
        line-height: 1.6;
        color: #bbb;
        margin: 20px 0;
    }
    .phrase-box {
        font-style: italic;
        border-top: 1px solid #333;
        border-bottom: 1px solid #333;
        padding: 20px 0;
        margin: 40px 0;
        text-align: center;
        color: #fff;
    }
    </style>
""", unsafe_allow_html=True)

if 'paso' not in st.session_state:
    st.session_state.paso = 'portada'

# --- 1. PORTADA EDITORIAL ---
if st.session_state.paso == 'portada':
    st.markdown('<h1 class="editorial-title">VANMAR PRO</h1>', unsafe_allow_html=True)
    st.markdown('<p class="editorial-subtitle">Gestión profesional de trámites vehiculares</p>', unsafe_allow_html=True)
    
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    
    # Enlace Real de Google
    login_url = f"https://accounts.google.com/o/oauth2/auth?client_id={CLIENT_ID}&response_type=code&scope=openid%20email%20profile&redirect_uri={REDIRECT_URI}&prompt=select_account"
    
    st.markdown(f'''
        <a href="{login_url}" target="_self" style="text-decoration:none;">
            <div style="border: 1px solid white; color: white; padding: 15px; text-align: center; font-weight: 600; text-transform: uppercase; letter-spacing: 2px;">
                Acceso vía Google Cloud
            </div>
        </a>
    ''', unsafe_allow_html=True)
    
    st.write("")
    if st.button("SOLICITAR ACCESO MANUAL"):
        st.session_state.paso = 'terminos'
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# --- 2. TÉRMINOS Y PRIVACIDAD ---
elif st.session_state.paso == 'terminos':
    st.markdown('<h2 style="font-family:Playfair Display; font-size:2rem;">Protocolo de Privacidad</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="privacy-box">
        Este documento garantiza que toda identidad y dato gestionado dentro de VANMAR PRO 
        está sujeto a leyes de protección de datos internacionales. La confidencialidad 
        de nuestros aliados es el activo más valioso de nuestra firma.
    </div>
    """, unsafe_allow_html=True)
    
    check = st.checkbox("Acepto el compromiso de confidencialidad")
    
    if st.button("CONTINUAR"):
        if check:
            st.session_state.paso = 'registro'
            st.rerun()
        else:
            st.error("Es necesario validar la palomita de privacidad.")

# --- 3. REGISTRO ---
elif st.session_state.paso == 'registro':
    st.markdown('<h2 style="font-family:Playfair Display;">Identificación</h2>', unsafe_allow_html=True)
    mail = st.text_input("Correo electrónico")
    whatsapp = st.text_input("WhatsApp de contacto")
    
    if st.button("VERIFICAR PERFIL"):
        if "@" in mail and len(whatsapp) >= 10:
            st.session_state.paso = 'final'
            st.rerun()

# --- 4. CIERRE EDITORIAL Y FRASE ---
elif st.session_state.paso == 'final':
    st.markdown('<h1 class="editorial-title">ÉXITO</h1>', unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class="phrase-box">
        "El éxito no es solo llegar al destino, sino la precisión y la integridad con la que recorres cada trámite del camino."
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    ### Propósito VANMAR:
    * **Fuerza:** Ejecuta con la potencia de un motor de alto rendimiento.
    * **Discreción:** La privacidad de tu equipo es la base de tu imperio.
    * **Gratitud:** Agradece a Dios por la visión de orden y excelencia que hoy lideras.
    """)
