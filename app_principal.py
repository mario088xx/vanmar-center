import streamlit as st

# --- CONFIGURACIÓN DE IDENTIDAD ---
CLIENT_ID = "98293623725-oaj0p863lnqkiuhoafv619st5gm57fsk.apps.googleusercontent.com"
REDIRECT_URI = "https://vanmar-center.streamlit.app"

st.set_page_config(page_title="VANMAR PRO", layout="centered")

# --- DISEÑO EDITORIAL HÍBRIDO (CSS) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Inter:wght@300;400;600&display=swap');
    
    .stApp { background-color: #050505; color: #E0E0E0; font-family: 'Inter', sans-serif; }
    
    .header-logo {
        text-align: center;
        padding: 40px 0 20px 0;
    }
    .title-main {
        font-family: 'Playfair Display', serif;
        font-size: 3rem;
        color: white;
        margin-bottom: 0px;
    }
    .slogan {
        text-transform: uppercase;
        letter-spacing: 3px;
        font-size: 0.75rem;
        color: #888;
        margin-bottom: 40px;
    }
    .icon-row {
        display: flex;
        justify-content: space-around;
        margin: 30px 0;
        text-align: center;
    }
    .icon-item { color: #4285F4; font-size: 0.8rem; }
    
    .card-editorial {
        background: #111;
        padding: 30px;
        border: 1px solid #222;
        border-radius: 5px;
    }
    .privacy-box {
        background: #000;
        padding: 15px;
        border-left: 3px solid #4285F4;
        font-size: 0.85rem;
        color: #999;
        margin: 20px 0;
    }
    </style>
""", unsafe_allow_html=True)

if 'paso' not in st.session_state:
    st.session_state.paso = 'inicio'

# --- 1. PORTADA ESTILO APP/EDITORIAL ---
if st.session_state.paso == 'inicio':
    st.markdown('<div class="header-logo">', unsafe_allow_html=True)
    st.markdown('<h1 class="title-main">VANMAR <span style="color:#4285F4">PRO</span></h1>', unsafe_allow_html=True)
    st.markdown('<p class="slogan">Gestión profesional de trámites vehiculares</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Fila de Iconos (Como en tu imagen)
    st.markdown("""
        <div class="icon-row">
            <div class="icon-item">🚗<br>Trámites</div>
            <div class="icon-item">📄<br>Documentos</div>
            <div class="icon-item">✅<br>Control</div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="card-editorial">', unsafe_allow_html=True)
    
    # Botón Google Cloud Real
    login_url = f"https://accounts.google.com/o/oauth2/auth?client_id={CLIENT_ID}&response_type=code&scope=openid%20email%20profile&redirect_uri={REDIRECT_URI}&prompt=select_account"
    
    st.markdown(f'''
        <a href="{login_url}" target="_self" style="text-decoration:none;">
            <div style="background-color: #4285F4; color: white; padding: 15px; border-radius: 5px; text-align: center; font-weight: 600; letter-spacing: 1px;">
                CONTINUE WITH GOOGLE
            </div>
        </a>
    ''', unsafe_allow_html=True)
    
    st.markdown("<p style='text-align:center; margin: 20px 0; color:#444;'>— O —</p>", unsafe_allow_html=True)
    
    if st.button("ACCESO MANUAL / ALIADOS", use_container_width=True):
        st.session_state.paso = 'privacidad'
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# --- 2. PRIVACIDAD (EL DOCUMENTO) ---
elif st.session_state.paso == 'privacidad':
    st.markdown('<h2 style="font-family:Playfair Display;">Protocolo de Seguridad</h2>', unsafe_allow_html=True)
    st.markdown("""
        <div class="privacy-box">
            Toda información gestionada en este portal está sujeta a estricta confidencialidad. 
            La identidad de nuestros gestores y los datos vehiculares están protegidos bajo cifrado.
        </div>
    """, unsafe_allow_html=True)
    
    aceptar = st.checkbox("Acepto el compromiso de privacidad")
    
    if st.button("CONTINUAR"):
        if aceptar:
            st.session_state.paso = 'registro'
            st.rerun()
        else:
            st.error("Es obligatorio marcar la palomita de privacidad.")

# --- 3. REGISTRO MANUAL ---
elif st.session_state.paso == 'registro':
    st.markdown('<h2 style="font-family:Playfair Display;">Identificación</h2>', unsafe_allow_html=True)
    email = st.text_input("Email corporativo")
    whatsapp = st.text_input("WhatsApp (10 dígitos)")
    
    if st.button("SOLICITAR ENTRADA"):
        if "@" in email and len(whatsapp) >= 10:
            st.session_state.paso = 'exito'
            st.rerun()

# --- 4. CIERRE CON FILOSOFÍA ---
elif st.session_state.paso == 'exito':
    st.balloons()
    st.markdown('<h1 style="font-family:Playfair Display; text-align:center;">ACCESO AUTORIZADO</h1>', unsafe_allow_html=True)
    st.write("---")
    
    st.markdown("""
        <div style="font-style: italic; text-align: center; padding: 20px; border: 1px solid #333; margin: 20px 0;">
            "El éxito no es solo llegar al destino, sino la precisión y la integridad con la que recorres cada trámite del camino."
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    ### 💡 Guía de Vida VANMAR:
    * **Fuerza:** La presión constante es lo que convierte el carbón en diamante.
    * **Discreción:** Tu palabra y la privacidad de tus datos son tu firma.
    * **Propósito:** Cada trámite bien hecho es un paso hacia la libertad financiera.
    * **Agradece a Dios por la capacidad de crear sistemas que sirven a otros con excelencia.**
    """)
