import streamlit as st

# --- 1. VARIABLES (Las llaves del sistema) ---
# Aquí guardamos los datos que Google necesita identificar
CLIENT_ID = "98293623725-oaj0p863lnqkiuhoafv619st5gm57fsk.apps.googleusercontent.com"
REDIRECT_URI = "https://vanmar-center.streamlit.app"

# --- 2. CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(page_title="VANMAR PRO", layout="centered")

# --- 3. CONSTRUCCIÓN DEL ENLACE "FORZADO" ---
# Esto crea la dirección que hace que la ventana de Google aparezca de verdad
login_url = (
    f"https://accounts.google.com/o/oauth2/auth?"
    f"client_id={CLIENT_ID}&"
    f"status=inline&"
    f"response_type=code&"
    f"scope=openid%20email%20profile&"
    f"redirect_uri={REDIRECT_URI}&"
    f"prompt=select_account"
)

# --- 4. DISEÑO DE LA PANTALLA ---
st.title("VANMAR PRO")
st.write("Portal de Gestión y Operaciones")

# El botón que usa el enlace que construimos arriba
st.markdown(f'''
    <a href="{login_url}" target="_self" style="text-decoration:none;">
        <div style="background-color: white; color: black; padding: 15px; border-radius: 10px; text-align: center; font-weight: bold; border: 1px solid #4285F4;">
            CONTINUAR CON GOOGLE 🌐
        </div>
    </a>
''', unsafe_allow_html=True)
