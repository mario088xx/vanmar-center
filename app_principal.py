import streamlit as st
import re
import random

# --- CONFIGURACIÓN VANMAR CENTER LUXURY ---
st.set_page_config(page_title="VANMAR CENTER", page_icon="✅", layout="centered")

def es_correo_valido(correo):
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(patron, correo) is not None

# CSS Estilo Apple Dark Mode - Blindado
st.markdown("""
    <style>
    .stApp { background: radial-gradient(circle at center, #1a1a1a 0%, #000000 100%); color: white; }
    .header-box { text-align: center; padding: 20px 0; }
    .icon-success { font-size: 3.5rem; filter: drop-shadow(0 0 10px #0071E3); display: block; margin-bottom: 10px; }
    h1 { font-size: 2.2rem !important; font-weight: 800; letter-spacing: -1px; margin-bottom: 5px; color: white; }
    
    .frase-container {
        margin: 25px 0; padding: 15px; border-left: 4px solid #0071E3;
        background: rgba(0, 113, 227, 0.08); border-radius: 0 12px 12px 0; text-align: left;
    }
    .frase-text { color: #FFFFFF; font-style: italic; font-size: 1.1rem; margin: 0; line-height: 1.4; }

    .glass-panel {
        background: rgba(255, 255, 255, 0.03); backdrop-filter: blur(20px); -webkit-backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.1); padding: 30px; border-radius: 20px;
    }

    div.stButton > button {
        background: #0071E3 !important; color: white !important;
        border-radius: 12px !important; font-weight: 700 !important;
        height: 55px; width: 100%; border: none !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- MEMORIA DEL SISTEMA ---
if 'auth' not in st.session_state: st.session_state.auth = False
if 'user' not in st.session_state: st.session_state.user = ""
if 'view' not in st.session_state: st.session_state.view = "login"
if 'pin_generado' not in st.session_state: st.session_state.pin_generado = "1234"

# --- ENCABEZADO CON ICONOS Y FRASE ---
st.markdown("""
    <div class='header-box'>
        <span class='icon-success'>📂✅</span>
        <h1>VANMAR CENTER</h1>
        <p style='color:#0071E3; font-weight:700; letter-spacing:3px; font-size:0.75rem;'>GESTIÓN VEHICULAR</p>
        <div class='frase-container'>
            <p class='frase-text'>"La disciplina es el puente entre tus metas y tus logros."</p>
        </div>
    </div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([0.1, 2, 0.1])

with col2:
    if not st.session_state.auth and st.session_state.view == "login":
        st.markdown('<div class="glass-panel">', unsafe_allow_html=True)
        u_nom = st.text_input("USUARIO", placeholder="Nombre del operador")
        u_pin = st.text_input("PIN DE ACCESO", type="password", placeholder="****")
        if st.button("INICIAR SESIÓN"):
            if u_pin == st.session_state.pin_generado and u_nom != "":
                st.session_state.auth = True
                st.session_state.user = u_nom
                st.rerun()
            else: st.error("Acceso denegado")
        st.write("---")
        if st.button("📝 REGISTRAR NUEVO ALIADO"):
            st.session_state.view = "registro"
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    elif not st.session_state.auth and st.session_state.view == "registro":
        st.markdown('<div class="glass-panel">', unsafe_allow_html=True)
        st.subheader("Registro de Aliado")
        reg_nom = st.text_input("Nombre")
        reg_mail = st.text_input("Correo")
        if st.button("GENERAR PIN Y REGISTRAR"):
            if reg_nom and es_correo_valido(reg_mail):
                nuevo_pin = str(random.randint(1000, 9999))
                st.session_state.pin_generado = nuevo_pin
                st.session_state.user = reg_nom
                st.markdown(f"""
                    <div style='text-align:center; padding:15px; border:1px solid #0071E3; border-radius:10px; background:rgba(0,113,227,0.1);'>
                        <p style='margin:0;'>¡Registro Exitoso!</p>
                        <div style='background:white; color:black; font-size:1.8rem; font-weight:800; padding:10px; border-radius:5px; display:inline-block; margin:10px 0;'>{nuevo_pin}</div>
                        <p style='color:#FFD700; font-size:0.75rem;'>⚠️ PIN SECRETO. NO COMPARTIR.</p>
                    </div>
                """, unsafe_allow_html=True)
            else: st.warning("Datos inválidos")
        if st.button("← VOLVER AL INICIO"):
            st.session_state.view = "login"
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    elif st.session_state.auth:
        st.markdown(f"<div class='glass-panel'><h3>Bienvenido, {st.session_state.user.upper()}</h3>", unsafe_allow_html=True)
        c1, c2 = st.columns(2)
        with c1: st.button("📂 TRAMITES")
        with c2: st.button("🤝 ALIANZAS")
        if st.button("CERRAR SESIÓN"):
            st.session_state.auth = False
            st.session_state.view = "login"
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)