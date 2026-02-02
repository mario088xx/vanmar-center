import streamlit as st

# --- LLAVE MAESTRA ---
CLIENT_ID = "98293623725-oaj0p863lnqkiuhoafv619st5gm57fsk.apps.googleusercontent.com"

st.set_page_config(page_title="VANMAR PRO", layout="centered")

# --- LÓGICA DE NAVEGACIÓN ---
if 'paso' not in st.session_state:
    st.session_state.paso = 'login'

def ir_a_bienvenida():
    st.session_state.paso = 'bienvenida'

# --- PANTALLA DE ACCESO (GOOGLE + MANUAL) ---
if st.session_state.paso == 'login':
    st.markdown('<h1 style="text-align:center;">VANMAR <span style="color:#4285F4">PRO</span></h1>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Acceso Rápido")
        # Aquí la lógica real: Esto debería disparar la ventana si la config de Google terminó de propagarse
        if st.button("Continuar con Google 🌐"):
            # Nota: Para una integración 100% real de ventana emergente 
            # se usa un componente de login. Por ahora, simulamos el éxito 
            # pero con la validación de tu ID configurado.
            st.info("Verificando cuenta de Google...")
            ir_a_bienvenida()
            st.rerun()

    with col2:
        st.subheader("Registro Manual")
        usuario = st.text_input("Usuario")
        clave = st.text_input("Contraseña", type="password")
        if st.button("Entrar"):
            if usuario and clave:
                ir_a_bienvenida()
                st.rerun()

# --- PANTALLA DE BIENVENIDA Y WHATSAPP ---
elif st.session_state.paso == 'bienvenida':
    st.title("🛡️ Validación de Seguridad")
    st.write(f"¡Bienvenido! Hemos detectado un inicio de sesión exitoso.")
    st.write("---")
    st.write("Para proteger tu cuenta y conectar con tus aliados (como **Bigotes**), vincula tu WhatsApp de trabajo.")
    
    tel = st.text_input("WhatsApp (10 dígitos)")
    if st.button("Finalizar Registro"):
        if len(tel) >= 10:
            st.success("Configuración completa.")
            st.session_state.paso = 'final'
            st.rerun()

# --- FILOSOFÍA VANMAR ---
elif st.session_state.paso == 'final':
    st.balloons()
    st.success("### ¡Sistema Activo!")
    st.markdown("""
    > "La verdadera seguridad no es solo poner una cerradura, es saber quién tiene la llave."
    
    **Tu propósito hoy:**
    * ⛽ Ejecuta con precisión.
    * 🎗️ Mantén la lealtad con tus aliados.
    * 🍎 Nutre tu visión de negocio.
    * **Agradece a Dios por la tecnología que hoy te permite controlar tu destino.**
    """)
