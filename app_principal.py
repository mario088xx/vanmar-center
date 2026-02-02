import streamlit as st

# --- 1. IDENTIDAD DEL SISTEMA ---
CLIENT_ID = "98293623725-oaj0p863lnqkiuhoafv619st5gm57fsk.apps.googleusercontent.com"
# Definimos la URL sin espacios ni errores
REDIRECT_URI = "https://vanmar-center.streamlit.app"

st.set_page_config(page_title="VANMAR PRO", layout="centered")

# --- 2. CONSTRUCCIÓN DEL ENLACE DE ACCESO ---
# Esta es la 'llave' que Google debe validar
login_url = (
    f"https://accounts.google.com/o/oauth2/auth?"
    f"client_id={CLIENT_ID}&"
    f"response_type=code&"
    f"scope=openid%20email%20profile&"
    f"redirect_uri={REDIRECT_URI}&"
    f"prompt=select_account"
)

# --- 3. INTERFAZ PROFESIONAL ---
st.markdown("<h1 style='text-align: center;'>VANMAR <span style='color:#4285F4'>PRO</span></h1>", unsafe_allow_html=True)
st.write("---")

st.markdown(f'''
    <div style="text-align: center;">
        <p>Portal de Gestión de Activos y Seguridad</p>
        <a href="{login_url}" target="_self" style="text-decoration: none;">
            <div style="background-color: white; color: #1f2937; padding: 15px; border-radius: 10px; font-weight: bold; border: 1px solid #4285F4; display: inline-block; width: 80%;">
                CONTINUAR CON GOOGLE 🌐
            </div>
        </a>
    </div>
''', unsafe_allow_html=True)

# --- 4. PRIVACIDAD ---
st.info("Su conexión está protegida bajo protocolos de cifrado de Google.")
