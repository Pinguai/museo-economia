import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Máquina del Tiempo Económica", page_icon="🚀")

st.title("🚀 La Máquina del Tiempo Económica")
st.markdown("### Concepto: **La Inflación**")

with st.sidebar:
    st.header("Configuración")
    monto_inicial = st.number_input("¿Cuánto dinero tienes hoy? ($)", min_value=1, value=1000)
    anios = st.slider("¿Cuántos años al futuro?", 1, 30, 10)
    tasa_inflacion = st.slider("Tasa de inflación anual (%)", 1.0, 20.0, 5.0) / 100

# Cálculo
anios_list = list(range(anios + 1))
valores = [monto_inicial / ((1 + tasa_inflacion) ** t) for t in anios_list]
valor_final = valores[-1]

# Interfaz Principal
col1, col2 = st.columns(2)
col1.metric("Valor Nominal", f"${monto_inicial:,.2f}")
col2.metric("Valor Real (Futuro)", f"${valor_final:,.2f}", f"-{((monto_inicial-valor_final)/monto_inicial)*100:.1f}%")

st.write(f"En {anios} años, tus ${monto_inicial:,.2f} comprarán lo que hoy compras con **${valor_final:,.2f}**.")

# Gráfica
df = pd.DataFrame({"Año": anios_list, "Valor Real": valores})
st.line_chart(df.set_index("Año"))

st.warning("⚠️ El ahorro estático es una pérdida garantizada. ¿Vas a emprender o vas a dejar que tu dinero muera?")