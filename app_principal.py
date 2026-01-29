import streamlit as st
import pandas as pd
from datetime import datetime

# Configuración Pro
st.set_page_config(page_title="VANMAR PRO Dashboard", layout="wide")

# ESTILOS CSS PARA DASHBOARD LIMPIO
st.markdown("""
    <style>
    .kpi-card {
        background-color: white; padding: 20px; border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1); text-align: center;
        border-top: 5px solid #007AFF;
    }
    .kpi-value { font-size: 24px; font-weight: bold; color: #1d1d1f; }
    .kpi-label { font-size: 14px; color: #86868b; }
    .tramite-card {
        background-color: #f9f9fb; padding: 15px; border-radius: 12px;
        margin-bottom: 10px; border-left: 8px solid #34C759;
    }
    </style>
    """, unsafe_allow_html=True)

# --- BASE DE DATOS TEMPORAL (Hoy conectaremos Google Sheets) ---
if 'db_tramites' not in st.session_state:
    st.session_state.db_tramites = [
        {"id": 1, "tipo": "Alta", "placas": "MEX-123-A", "auto": "Nissan Sentra 2020", "aliado": "BIGOTES", "status": "Agendado", "monto": 850},
        {"id": 2, "tipo": "Cambio Propietario", "placas": "ABC-456-B", "auto": "Toyota Corolla 2019", "aliado": "LIZ", "status": "Recibido", "monto": 1200}
    ]

# --- VISTA DE DASHBOARD ---
st.title("📊 Panel de Control VANMAR PRO")

# 1. FILA DE INDICADORES (KPIs)
col1, col2, col3, col4, col5 = st.columns(5)
with col1: st.markdown('<div class="kpi-card"><div class="kpi-value">2</div><div class="kpi-label">RECIBIDOS</div></div>', unsafe_allow_html=True)
with col2: st.markdown('<div class="kpi-card"><div class="kpi-value">1</div><div class="kpi-label">AGENDADOS</div></div>', unsafe_allow_html=True)
with col3: st.markdown('<div class="kpi-card" style="border-top-color: #34C759;"><div class="kpi-value">0</div><div class="kpi-label">CONCLUIDOS</div></div>', unsafe_allow_html=True)
with col4: st.markdown('<div class="kpi-card" style="border-top-color: #FF9500;"><div class="kpi-value">$2,050</div><div class="kpi-label">POR COBRAR</div></div>', unsafe_allow_html=True)
with col5:
    if st.button("➕ Nuevo Trámite"):
        st.session_state.step = 'main' # Regresa al flujo de carga
        st.rerun()

st.write("---")

# 2. BUSCADOR Y LISTA
search = st.text_input("🔍 Buscar por placas, gestoría o folio...", placeholder="Ej: BIGOTES")

st.subheader("Trámites Recientes")

for t in st.session_state.db_tramites:
    # Filtro de búsqueda simple
    if search.lower() in t['aliado'].lower() or search.lower() in t['placas'].lower():
        color = "#007AFF" if t['status'] == "Agendado" else "#FF3B30"
        st.markdown(f"""
            <div class="tramite-card" style="border-left-color: {color}">
                <div style="display: flex; justify-content: space-between;">
                    <b>{t['tipo']}</b> <span>${t['monto']}</span>
                </div>
                <div style="font-size: 13px; color: #666;">
                    🚗 {t['placas']} • {t['auto']}<br>
                    👤 Gestoría: <b>{t['aliado']}</b><br>
                    📍 Estatus: <span style="color:{color}; font-weight:bold;">{t['status']}</span>
                </div>
            </div>
        """, unsafe_allow_html=True)

# 3. NOTA PROACTIVA
st.info("💡 Consejo VANMAR: Recuerda revisar los expedientes marcados en rojo antes de salir al módulo.")
