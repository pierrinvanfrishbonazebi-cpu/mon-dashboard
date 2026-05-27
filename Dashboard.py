import streamlit as st
import plotly.express as px
import pandas as pd

st.title("📊 Mon Premier Dashboard")

# --- KPIs ---
col1, col2, col3 = st.columns(3)

col1.metric("💰 Chiffre d'affaires", "301 500 FCFA", "+12.4%")
col2.metric("🛒 Commandes", "1 847", "+8.1%")
col3.metric("👥 Clients actifs", "4 290", "-2.3%")

# --- Graphique ---
df = pd.DataFrame({
    "Mois": ["Jan", "Fév", "Mar", "Avr", "Mai"],
    "Ventes": [42000, 47500, 38000, 55000, 61000]
})

fig = px.bar(df, x="Mois", y="Ventes", title="Ventes mensuelles")
st.plotly_chart(fig)