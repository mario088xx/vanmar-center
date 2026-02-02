import streamlit as st

# --- CONFIGURACIÓN DE IDENTIDAD ---
CLIENT_ID = "98293623725-oaj0p863lnqkiuhoafv619st5gm57fsk.apps.googleusercontent.com"
REDIRECT_URI = "https://vanmar-center.streamlit.app/"

st.set_page_config(page_title="VANMAR PRO", layout="centered")

# --- CSS: ESTÉTICA DE ALTA GAMA ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@100;300;600&display=swap');
    
    .stApp {
        background: radial-gradient(circle at center, #111827 0%, #030712 100%);
        color: #f9fafb;
        font-family: 'Inter', sans-serif;
    }
    
    /* Contenedor del Logo */
    .logo-container {
        text-align: center;
        margin-top: 20px;
        color: #94a3b8;
        font-size: 3rem;
        opacity: 0.8;
    }
    
    .main-title {
        font-size: 3rem;
        font-weight: 100;
        letter-spacing: 4px;
        text-align: center;
        color: #ffffff;
        margin-top: 10px;
        margin-bottom: 0px;
    }
    
    .sub-title {
        text-transform: uppercase;
        letter-spacing: 3px;
        font-size: 0.65rem;
        color: #64748b;
        text-align: center;
        margin-bottom: 50px;
    }

    /* Botones Uniformes */
    .custom-button {
        display: block;
        width: 100%;
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(8px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        color: #f8fafc;
        text-align: center;
        padding: 16px 0;
        border-radius: 8px;
        text-decoration: none;
        font-weight: 300;
        letter-spacing: 1px;
        font-size: 0.8rem;
        transition: all 0.4s ease;
        margin-bottom: 12px;
        cursor: pointer;
    }
    .custom-button:hover {
        background: rgba(255, 255, 255, 0.08);
