import streamlit as st
import pandas as pd
from datetime import datetime
import urllib.parse

# CONFIGURACIÓN DE PÁGINA ESTILO APPLE
st.set_page_config(page_title="VANMAR PRO", page_icon="💎", layout="centered")

# ESTILOS PERSONALIZADOS PARA EL LOGIN PROFESIONAL
st.markdown("""
    <style>
    .stButton>button { width: 100%; border-radius: 12px; height: 3.5em; background-color: #007AFF; color: white; border: none; font-weight: bold; }
    .stTextInput>div>div>input { border-radius: 8px; border: 1px solid #ddd; padding: 12px; }
    .main-title { text-align: center; color: #1d1d1f; font-size: 28px; font-weight: 700; margin-bottom: 5px; }
    .sub-title { text-align: center; color: #86868b; font-size: 16px; margin-bottom: 30px; }
    .icon-container { display: flex; justify-content: space-around; text-align: center; margin-bottom: 30px; }
    .icon-box { font-size: 40px; }
    .icon-label { font-size: 12px; color: #1d1d1f; margin-top: 5px; }
    hr { margin: 25px 0; border: 0; border-top: 1px solid #eee; }
    </style>
    """, unsafe_allow_html=True)

# --- ESTADOS DE SESIÓN ---
if 'step' not in st.session_state:
    st.session_state.step = 'login'
if 'user_wa' not in st.session_state:
    st.session_state.user_wa = ""

# --- FUNCIÓN WHATSAPP ---
def send_wa(num, msg):
    return f"https://wa.me/{num}?text={urllib.parse.quote(msg)}"

# --- 1. PANTALLA DE LOGIN (REDiseñada) ---
if st.session_state.step == 'login':
    # Encabezado Visual
    st.markdown('<p class="main-title">VANMAR PRO</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">Bienvenido a tu gestión vehicular profesional.<br>Registrate para continuar.</p>', unsafe_allow_html=True)
    
    # Fila de Iconos (Carro, Doc, OK)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<div style="text-align:center"><span style="font-size:40px;">🚗</span><br><span style="font-size:12px;">Trámites</span></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div style="text-align:center"><span style="font-size:40px;">📄</span><br><span style="font-size:12px;">Documentos</span></div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div style="text-align:center"><span style="font-size:40px;">✅</span><br><span style="font-size:12px;">Control</span></div>', unsafe_allow_html=True)
    
    st.write("") # Espaciador
    
    # Botón Google
    if st.button("Continue with Google 🌐"):
        st.session_state.step = 'wa_config'
        st.rerun()
        
    st.markdown('<p style="text-align:center; color:#86868b;">— o —</p>', unsafe_allow_html=True)
    
    # Formulario Email
    email = st.text_input("Email", placeholder="tu@ejemplo.com")
    password = st.text_input("Password", type="password", placeholder="••••••••")
    
    if st.button("Sign in"):
        if email and password:
            st.session_state.step = 'wa_config'
            st.rerun()
        else:
            st.error("Por favor completa los campos")

    st.markdown('<p style="text-align:center; font-size:14px;"><a href="#">Forgot password?</a></p>', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center; font-size:14px; margin-top:10px;">Need an account? <a href="#">Sign up</a></p>', unsafe_allow_html=True)

# --- 2. REGISTRO DE WHATSAPP ---
elif st.session_state.step == 'wa_config':
    st.markdown("### 📲 Configura tu WhatsApp")
    st.write("Necesitamos tu número para enviarte notificaciones de tus trámites.")
    num = st.text_input("Número de 10 dígitos", placeholder="5512345678")
    
    if st.button("Confirmar Número"):
        if len(num) == 10:
            st.session_state.user_wa = "52" + num
            st.session_state.step = 'main'
            st.rerun()
        else:
            st.error("Ingresa un número válido")

# --- 3. FLUJO DE TRABAJO (PROPIO/ALIADOS) ---
elif st.session_state.step == 'main':
    st.title("🚀 Nuevo Trámite")
    st.write("### 1. Sube tu Cita")
    cita = st.file_uploader("Arrastra aquí el documento", type=['pdf', 'jpg', 'png'])
    
    if cita:
        st.success("Cita detectada.")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("PROPIO"):
                st.session_state.tipo = "PROPIO"
                st.session_state.step = 'upload'
                st.rerun()
        with col2:
            if st.button("ALIADOS"):
                st.session_state.tipo = "ALIADOS"
                st.session_state.step = 'upload'
                st.rerun()

# --- 4. EXPEDIENTE Y VALIDACIÓN ---
elif st.session_state.step == 'upload':
    st.title(f"📂 Expediente {st.session_state.tipo}")
    
    aliado = ""
    if st.session_state.tipo == "ALIADOS":
        aliados = ["BIGOTES", "LIZ", "EMILIO", "PASCUAL", "ADRI", "ALONZO", "RAQUEL", "ALBERTO", "TOCAYO ISRA", "VICTOR", "FELIX", "GEMELO", "OTRO"]
        aliado = st.selectbox("Selecciona al Aliado:", aliados)

    # Simulación de carga
    solicitud = st.file_uploader("Solicitud")
    pago = st.file_uploader("Comprobante de Pago")
    ine = st.file_uploader("Identificación (INE)")
    
    if st.button("Validar y Finalizar"):
        if not ine or not pago:
            st.error("Faltan documentos críticos.")
            if st.session_state.tipo == "ALIADOS":
                st.warning(f"¿Quieres que le avise a {aliado}?")
                msg = f"Oye {aliado}, falta documento de este trámite. Enviado desde VANMAR PRO."
                st.markdown(f"[📲 Avisar a {aliado} por WhatsApp]({send_wa('525500000000', msg)})")
        else:
            st.session_state.step = 'final'
            st.rerun()

# --- 5. ASIGNACIÓN FINAL ---
elif st.session_state.step == 'final':
    st.title("✅ Asignación")
    resp = st.radio("¿Quién concluye?", ["VAN", "MAR", "OTRO"])
    
    if st.button("Terminar y Notificar"):
        mensaje = f"¡Buenos días! Tienes trámites con {resp}. No olvides gasolina, cinturón y agradecer a Dios. ¡Éxito! - VANMAR PRO"
        st.markdown(f"[📲 Enviar Resumen a WhatsApp]({send_wa(st.session_state.user_wa, mensaje)})")
        st.balloons()
