"""Exibe o conteúdo da página Orçamento Excedido."""
from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st
from data.controller import get_project_orcamento_excedente_por_semestre


def orcamento_excedido_page() -> None:
    """Exibir o conteúdo da página Orçamento Excedido."""
    st.title("Porcentagem de Projetos que Excederam o Orçamento por Semestre")

    excedente_data = get_project_orcamento_excedente_por_semestre()
    if excedente_data:
        excedente_data = pd.DataFrame(
            excedente_data,
            columns=['Ano',
                    'Semestre',
                    'Projetos_Total',
                    'Projetos_Excedidos',
                    'Porcentagem_Excedidos',
                    ],
        )

        with st.expander("Ver detalhes"):
            st.write("Dados dos Projetos que Excederam o Orçamento por Semestre:")
            st.write(excedente_data)

            try:
                with Path('/workspace/scripts/porcentagem_excedentes.sql').open() as file:
                    porcentagem_excedentes = file.read()

                st.markdown("### Consulta SQL")
                st.code(porcentagem_excedentes, language='sql')
            except FileNotFoundError:
                st.warning("Script SQL Somente aparece em desenvolvimento.")

        fig = px.bar(
            excedente_data,
            x='Semestre',
            y='Porcentagem_Excedidos',
            color='Ano',
            text='Porcentagem_Excedidos',
            title="Porcentagem de Projetos que Excederam o Orçamento por Semestre",
            labels={'Porcentagem_Excedidos': '% Excedido', 'Semestre': 'Semestre'},
            barmode='group',
        )

        fig.update_traces(texttemplate='%{text:.2f}%', textposition='outside')
        st.plotly_chart(fig)
    else:
        st.write("Nenhum projeto excedeu o orçamento nos últimos 2 anos.")
