# app.py
# Controle Financeiro Pessoal com Streamlit

import streamlit as st
import pandas as pd

# Título do site
st.title("💰 Controle Financeiro Pessoal")

# Lista para armazenar os gastos
if "gastos" not in st.session_state:
    st.session_state.gastos = []

# Formulário para adicionar gastos
st.header("Adicionar Gasto")

nome = st.text_input("Nome do gasto")
valor = st.number_input("Valor do gasto", min_value=0.0, format="%.2f")

if st.button("Adicionar"):
    st.session_state.gastos.append({
        "Nome": nome,
        "Valor": valor
    })

    st.success("Gasto adicionado com sucesso!")

# Mostrar tabela de gastos
st.header("📋 Lista de Gastos")

if len(st.session_state.gastos) > 0:

    df = pd.DataFrame(st.session_state.gastos)

    st.dataframe(df)

    # Total gasto
    total = df["Valor"].sum()

    st.subheader(f"💸 Total gasto: R$ {total:.2f}")

    # Gráfico
    st.header("📊 Gráfico de Gastos")

    st.bar_chart(df.set_index("Nome"))

else:
    st.info("Nenhum gasto cadastrado ainda.")
