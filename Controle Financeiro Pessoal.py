# app.py
# Controle Financeiro Pessoal com Streamlit

pip install streamlit pandas
streamlit run app.py
# app.py
# Controle Financeiro Completo com Streamlit

import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Controle Financeiro", layout="centered")

st.title("💰 Controle Financeiro Pessoal")

# =========================
# INICIALIZAÇÃO
# =========================

if "gastos" not in st.session_state:
    st.session_state.gastos = []

if "salario" not in st.session_state:
    st.session_state.salario = 0.0

# =========================
# SALÁRIO
# =========================

st.header("💵 Salário Mensal")

salario = st.number_input(
    "Digite quanto você ganha por mês:",
    min_value=0.0,
    format="%.2f",
    value=st.session_state.salario
)

st.session_state.salario = salario

# =========================
# ADICIONAR GASTOS
# =========================

st.header("➕ Adicionar Gasto")

nome = st.text_input("Nome do gasto")

valor = st.number_input(
    "Valor do gasto",
    min_value=0.0,
    format="%.2f"
)

categoria = st.selectbox(
    "Categoria",
    ["Alimentação", "Transporte", "Lazer", "Contas", "Saúde", "Outros"]
)

data = st.date_input("Data do gasto")

if st.button("Adicionar Gasto"):

    if nome != "":

        st.session_state.gastos.append({
            "Nome": nome,
            "Valor": valor,
            "Categoria": categoria,
            "Data": data.strftime("%d/%m/%Y"),
            "Mês": data.strftime("%m/%Y")
        })

        st.success("Gasto adicionado com sucesso!")

    else:
        st.error("Digite o nome do gasto.")

# =========================
# LISTA DE GASTOS
# =========================

st.header("📋 Lista de Gastos")

if len(st.session_state.gastos) > 0:

    df = pd.DataFrame(st.session_state.gastos)

    st.dataframe(df)

    # =========================
    # APAGAR GASTO
    # =========================

    st.subheader("🗑️ Apagar Gasto")

    gasto_para_apagar = st.selectbox(
        "Selecione um gasto para apagar:",
        df.index
    )

    if st.button("Apagar Gasto"):

        st.session_state.gastos.pop(gasto_para_apagar)

        st.success("Gasto apagado!")

        st.rerun()

    # =========================
    # FILTRO POR MÊS
    # =========================

    st.header("📅 Gastos por Mês")

    meses = df["Mês"].unique()

    mes_selecionado = st.selectbox(
        "Selecione o mês:",
        meses
    )

    df_mes = df[df["Mês"] == mes_selecionado]

    st.dataframe(df_mes)

    total_mes = df_mes["Valor"].sum()

    st.subheader(f"💸 Total gasto no mês: R$ {total_mes:.2f}")

    # =========================
    # DÉFICIT OU SOBRA
    # =========================

    saldo = salario - total_mes

    if saldo > 0:
        st.success(f"✅ Você ainda possui R$ {saldo:.2f} sobrando.")
    elif saldo < 0:
        st.error(f"⚠️ Você está em déficit de R$ {abs(saldo):.2f}.")
    else:
        st.warning("Você gastou exatamente todo o salário.")

    # =========================
    # GRÁFICO MENSAL
    # =========================

    st.header("📊 Gráfico de Gastos Mensais")

    grafico = df.groupby("Mês")["Valor"].sum()

    st.bar_chart(grafico)

else:
    st.info("Nenhum gasto cadastrado ainda.")
