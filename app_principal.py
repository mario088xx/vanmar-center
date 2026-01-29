import streamlit as st
import pandas as pd
from datetime import datetime
import urllib.parse

# CONFIGURACIÓN DE PÁGINA ESTILO APPLE
st.set_page_config(page_title="VANMAR PRO", page_icon="💎", layout="centered")

# ESTILOS PERSONALIZADOS
st.markdown("""
    <style>
    .stButton>button { width: 100%; border-radius: 20px; height: 3em; background-color: #007AFF; color: white; }
    .stTextInput>div>div>input { border-radius: 10px; }
    .status-box { padding: 20px; border-radius: 15px; border: 1px solid #ddd; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

# --- LÓGICA DE ESTADO ---
if 'step' not in st.session_state:
    st.session_state.step = 'login'
if 'user_wa' not in st.session_state:
    st.session_state.user_wa = ""

# --- FUNCIONES DE APOYO ---
def send_wa(num, msg):
    text = urllib.parse.quote(msg)
    return f"https://wa.me/{num}?text={text}"

# --- 1. LOGIN & WHATSAPP CONFIG ---
if st.session_state.step == 'login':
    st.title("💎 Sign in to continue")
    st.subheader("VANMAR PRO | Gestión Vehicular")
    
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    
    if st.button("Sign in"):
        st.session_state.step = 'wa_config'
        st.rerun()

elif st.session_state.step == 'wa_config':
    st.title("📲 Configuración de Notificaciones")
    st.info("Registra tu WhatsApp de trabajo para recibir alertas y control de citas.")
    wa_num = st.text_input("Número de WhatsApp (10 dígitos)", placeholder="Ej: 5512345678")
    
    if st.button("Confirmar y Continuar"):
        if len(wa_num) == 10:
            st.session_state.user_wa = "52" + wa_num
            st.session_state.step = 'main'
            st.rerun()
        else:
            st.error("Por favor ingresa un número válido.")

# --- 2. PANTALLA PRINCIPAL (CARGA DE CITA) ---
elif st.session_state.step == 'main':
    st.title("🚀 Iniciar Nuevo Trámite")
    
    # DISPARADOR: CARGA DE CITA
    st.write("### 1. Sube la Cita para iniciar")
    cita_file = st.file_uploader("Arrastra aquí el documento de la Cita", type=['pdf', 'jpg', 'png'])
    
    if cita_file:
        st.success("Cita cargada correctamente.")
        
        st.write("### 2. ¿Quién solicita el trámite?")
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("PROPIO"):
                st.session_state.tipo_solicitante = "PROPIO"
                st.session_state.step = 'upload_docs'
                st.rerun()
        
        with col2:
            if st.button("ALIADOS"):
                st.session_state.tipo_solicitante = "ALIADOS"
                st.session_state.step = 'upload_docs'
                st.rerun()

# --- 3. CARGA DE DOCUMENTOS Y VALIDACIÓN ---
elif st.session_state.step == 'upload_docs':
    st.title(f"📂 Expediente: {st.session_state.tipo_solicitante}")
    
    aliado_nombre = ""
    if st.session_state.tipo_solicitante == "ALIADOS":
        aliados_list = ["BIGOTES", "LIZ", "EMILIO", "PASCUAL", "ADRI", "ALONZO", "RAQUEL", "ALBERTO", "TOCAYO ISRA", "VICTOR", "FELIX", "GEMELO", "OTRO (Manual)"]
        aliado_nombre = st.selectbox("¿De qué gestoría es este trámite?", aliados_list)
        if aliado_nombre == "OTRO (Manual)":
            aliado_nombre = st.text_input("Nombre de la gestoría")

    st.write("### Carga de documentos requeridos")
    solicitud = st.file_uploader("Solicitud de trámite")
    pago = st.file_uploader("Recibo de Pago")
    ine = st.file_uploader("INE / ID Oficial")
    denuncia = st.checkbox("¿Perdió placas? (Subir Baja/Denuncia)")
    denuncia_file = None
    if denuncia:
        denuncia_file = st.file_uploader("Constancia de denuncia")
        
    poder = None
    if st.session_state.tipo_solicitante == "ALIADOS":
        poder = st.file_uploader("Poder Notarial (Solo empresas)")

    # ESTRATEGIA PROACTIVA: DETECCIÓN DE FALTANTES
    if st.button("Validar Expediente"):
        faltantes = []
        if not solicitud: faltantes.append("Solicitud")
        if not pago: faltantes.append("Pago")
        if not ine: faltantes.append("INE")
        
        if faltantes:
            st.error(f"Faltan documentos: {', '.join(faltantes)}")
            if st.session_state.tipo_solicitante == "ALIADOS":
                st.warning(f"¿Quieres que le avise a {aliado_nombre} por ti?")
                msg_aliado = f"Hola {aliado_nombre}, detectamos que falta: {', '.join(faltantes)} para el trámite. Favor de enviarlo. \n\nMensaje enviado desde VANMAR PRO 💎"
                st.markdown(f"[📲 Avisar a {aliado_nombre} por WhatsApp]({send_wa('52', msg_aliado)})")
        else:
            st.success("¡Expediente Completo!")
            st.session_state.step = 'final'
            st.rerun()

# --- 4. ASIGNACIÓN Y CIERRE ---
elif st.session_state.step == 'final':
    st.title("✅ Asignación de Trámite")
    responsable = st.radio("¿Quién concluye este trámite?", ["VAN", "MAR", "OTRO"])
    
    if st.button("Finalizar y Notificar"):
        # MENSAJE DE LAS 7 AM / RESUMEN (SIMULADO PARA WHATSAPP)
        msg_resumen = f"✅ NUEVO TRÁMITE ASIGNADO A {responsable}\n\nNo olvides revisar gasolina, cinturón y agradecer a Dios. ¡Mucho éxito hoy! 🚀\n\nMensaje enviado desde VANMAR PRO"
        st.markdown(f"[📲 Enviar Resumen a mi WhatsApp]({send_wa(st.session_state.user_wa, msg_resumen)})")
        st.balloons()
        if st.button("Registrar otro trámite"):
            st.session_state.step = 'main'
            st.rerun()
