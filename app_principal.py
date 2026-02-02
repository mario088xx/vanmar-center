import streamlit as st

# --- CONFIGURACIÓN DE IDENTIDAD ---
CLIENT_ID = "98293623725-oaj0p863lnqkiuhoafv619st5gm57fsk.apps.googleusercontent.com"
REDIRECT_URI = "https://vanmar-center.streamlit.app/"

st.set_page_config(page_title="VANMAR PRO", layout="centered")

# --- DISEÑO EDITORIAL AMIGABLE (DEGRADADO Y TRANSPARENCIAS) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Inter:wght@300;400;600&display=swap');
    
    /* Fondo con degradado editorial suave */
    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #334155 100%);
        color: #f8fafc;
        font-family: 'Inter', sans-serif;
    }
    
    .title-vanmar { font-family: 'Playfair Display', serif; font-size: 3.2rem; color: #f1f5f9; text-align: center; margin-bottom: 5px; }
    .subtitle-vanmar { text-transform: uppercase; letter-spacing: 4px; font-size: 0.75rem; color: #94a3b8; text-align: center; margin-bottom: 45px; }
    
    /* Tarjeta con transparencia editorial (Glassmorphism) */
    .editorial-card {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(15px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 24px;
        padding: 40px;
        margin: 20px 0;
        box-shadow: 0 20px 50px rgba(0,0,0,0.3);
    }
    
    .google-btn-container {
        border: 1px solid rgba(255, 255, 255, 0.4);
        border-radius: 12px;
        padding: 14px;
        text-align: center;
        transition: all 0.3s ease;
        background: rgba(255, 255, 255, 0.05);
    }
    
    .google-btn-container:hover {
        background: rgba(255, 255, 255, 0.1);
        border-color: white;
    }
    
    .privacy-box {
        background: rgba(0, 0, 0, 0.2);
        padding: 20px;
        border-radius: 12px;
        font-size: 0.88rem;
        line-height: 1.7;
        color: #cbd5e1;
        height: 140px;
        overflow-y: scroll;
        border: 1px solid rgba(255, 255, 255, 0.05);
    }
    </style>
""", unsafe_allow_html=True)

if 'paso' not in st.session_state:
    st.session_state.paso = 'inicio'

# --- PANTALLA 1: PORTADA ---
if st.session_state.paso == 'inicio':
    st.markdown('<h1 class="title-vanmar">VANMAR PRO</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle-vanmar">Gestión profesional de trámites vehiculares</p>', unsafe_allow_html=True)
    
    st.markdown('<div class="editorial-card">', unsafe_allow_html=True)
    
    login_url = f"https://accounts.google.com/o/oauth2/auth?client_id={CLIENT_ID}&response_type=code&scope=openid%20email%20profile&redirect_uri={REDIRECT_URI}&prompt=select_account"
    
    st.markdown(f'''
        <a href="{login_url}" target="_self" style="text-decoration:none;">
            <div class="google-btn-container">
                <span style="color: white; font-weight: 500; letter-spacing: 1px;">CONTINUAR CON GOOGLE 🌐</span>
            </div>
        </a>
    ''', unsafe_allow_html=True)
    
    st.write("")
    if st.button("REGÍSTRATE"):
        st.session_state.paso = 'privacidad'
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# --- PANTALLA 2: PRIVACIDAD ---
elif st.session_state.paso == 'privacidad':
    st.markdown('<div class="editorial-card">', unsafe_allow_html=True)
    st.markdown('<h2 style="font-family:Playfair Display; color:white; margin-top:0;">Protocolo de Privacidad</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="privacy-box">
        <b>Compromiso de Confidencialidad:</b><br>
        En VANMAR PRO, la integridad de su información es el pilar de nuestra gestión. 
        Toda identidad y dato vehicular está protegido bajo estrictos estándares de cifrado. 
        Al continuar, usted acepta nuestro protocolo de manejo de datos para fines operativos exclusivos.
    </div>
    """, unsafe_allow_html=True)
    
    aceptar = st.checkbox("He leído y acepto los términos")
    
    if st.button("SIGUIENTE"):
        if aceptar:
            st.session_state.paso = 'registro_final'
            st.rerun()
        else:
            st.error("Es necesario validar los términos.")
    st.markdown('</div>', unsafe_allow_html=True)

# --- PANTALLA 3: REGISTRO FINAL ---
elif st.session_state.paso == 'registro_final':
    st.markdown('<div class="editorial-card">', unsafe_allow_html=True)
    st.markdown('<h2 style="font-family:Playfair Display; color:white; margin-top:0;">Identificación</h2>', unsafe_allow_html=True)
    correo = st.text_input("Correo electrónico corporativo")
    whatsapp = st.text_input("WhatsApp (10 dígitos)")
    
    if st.button("ACTIVAR PERFIL"):
        if "@" in correo and len(whatsapp) >= 10:
            st.session_state.paso = 'exito'
            st.rerun()

# --- PANTALLA 4: ÉXITO ---
elif st.session_state.paso == 'exito':
    st.balloons()
    st.markdown('<h1 class="title-vanmar" style="font-size:2.5rem;">BIENVENIDO</h1>', unsafe_allow_html=True)
    
    st.markdown("""
    <div style="font-style: italic; border-top: 1px solid rgba(255,255,255,0.1); border-bottom: 1px solid rgba(255,255,255,0.1); padding: 25px 0; margin: 30px 0; text-align: center; color: #f8fafc;">
        "El éxito no es solo llegar al destino, sino la precisión y la integridad con la que recorres cada trámite del camino."
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    **Propósito VANMAR:**
    * **Fuerza:** Ejecuta con la potencia de un motor de alto rendimiento.
    * **Lealtad:** La privacidad de tu equipo es la base de tu imperio.
    * **Gratitud:** Agradece a Dios por la visión de orden y excelencia que hoy lideras.
    """)
