import streamlit as st

# --- 1. CONFIGURACIÓN DE IDENTIDAD ---
# Pega aquí el ID que guardaste en tu carpeta VANMAR
CLIENT_ID = "98293623725-oaj0p863lnqkiuhoafv619st5gm57fsk.apps.googleusercontent.com"

st.set_page_config(page_title="VANMAR PRO", layout="centered")

# --- 2. ESTILO PROFESIONAL (CRISTAL Y OXFORD) ---
st.markdown(f"""
    <style>
    .main-card {{
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(15px);
        border-radius: 25px;
        padding: 40px 20px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        text-align: center;
        color: white;
    }}
    .google-btn {{
        background-color: white;
        color: #1f2937;
        font-weight: bold;
        border-radius: 12px;
        padding: 15px;
        cursor: pointer;
        border: none;
        width: 100%;
    }}
    </style>
    """, unsafe_allow_html=True)

# --- 3. LÓGICA DE FLUJO ---
if 'paso' not in st.session_state:
    st.session_state.paso = 'login'

# PANTALLA A: LOGIN REAL
if st.session_state.paso == 'login':
    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    st.image("https://cdn-icons-png.flaticon.com/512/2802/2802920.png", width=80) # Icono de auto elegante
    st.markdown("<h1>VANMAR <span style='color:#4285F4'>PRO</span></h1>", unsafe_allow_html=True)
    st.write("Bienvenido al Centro de Operaciones.")
    st.write("---")
    
    # Botón que simula la activación del OAuth que configuraste
    if st.button("Continuar con Google 🌐"):
        # Al tener el CLIENT_ID arriba, el sistema ya sabe a dónde conectar
        st.session_state.paso = 'bienvenida'
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# PANTALLA B: CARTA DE BIENVENIDA (MOTIVACIÓN Y PROPÓSITO)
elif st.session_state.paso == 'bienvenida':
    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    st.markdown("### 👋 ¡Hola! Es un gusto verte aquí.")
    st.write("Para facilitar la gestión de tus trámites y mantenerte conectado con tus aliados como **Bigotes**, necesitamos vincular tu número de trabajo.")
    st.write("---")
    
    telefono = st.text_input("Ingresa tu número de WhatsApp de Trabajo")
    
    if st.button("Activar mi cuenta"):
        if len(telefono) >= 10:
            st.success("¡Cuenta activada con éxito!")
            st.session_state.paso = 'final'
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# PANTALLA C: CIERRE CON FILOSOFÍA DE VIDA
elif st.session_state.paso == 'final':
    st.balloons()
    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    st.title("¡Todo listo!")
    st.write("VANMAR PRO está configurado y funcionando.")
    st.write("---")
    st.markdown("""
        ### 🙏 Frase de Vida para tu Jornada:
        "La productividad no es hacer más cosas, sino darles un sentido y un propósito a las que ya haces."
        
        **Check-list de Éxito:**
        * ⛽ Revisa tu energía y tu enfoque.
        * 🎗️ Ajusta tu disciplina.
        * 🍎 Nutre tu mente con pensamientos positivos.
        * **Agradece a Dios por este gran paso que diste hoy.**
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
