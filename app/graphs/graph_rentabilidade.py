"""Exibi o conteúdo da página Rentabilidade Líquida."""
from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st
from data.controller import get_projects
from utils.utils import generate_colors, get_project_ultimo_ano


def rentabilidade_liquida_page() -> None:
    """Exibi a page Rentabilidade Líquida."""
    st.title("Rentabilidade Líquida de Projetos")

    projects = get_projects(50)

    with st.spinner('Carregando dados dos projetos...'):

        project_ultimo_ano = get_project_ultimo_ano(projects)

        if project_ultimo_ano:
            projects_df = pd.DataFrame(project_ultimo_ano)
            with st.expander("Ver detalhes"):
                st.write("Total de projetos retornados pelo Banco:", len(projects))
                st.write("Total de projetos do último ano:", len(project_ultimo_ano))
                st.write("Dataframe dos projetos do último ano:")
                st.write(projects_df)

                script_path = Path('/workspace/scripts/rentabilidade_liquida.sql')
                try:
                    with script_path.open() as file:
                        rentabilidade_liquida_sql = file.read()

                    st.markdown("### Consulta SQL")
                    st.code(rentabilidade_liquida_sql, language='sql')
                except FileNotFoundError:
                    st.warning("Script SQL Somente aparece em desenvolvimento.")

            colors = generate_colors(len(projects_df))

            fig = px.bar(
                projects_df,
                x='nome',
                y='Rentabilidade_liquida',
                title='Rentabilidade Líquida dos Projetos do Último Ano',
                text='Rentabilidade_liquida',
                color='nome',
                color_discrete_sequence=colors,
            )

            fig.update_layout(
                xaxis_title='Nome do Projeto',
                yaxis_title='Rentabilidade Líquida',
                title='Rentabilidade Líquida dos Projetos do Último Ano',
                xaxis_tickangle=-45,
                font={'size': 14},
                margin={'t': 50, 'b': 150, 'l': 50, 'r': 50},
                height=600,
                showlegend=False,
            )

            fig.update_traces(
                texttemplate='%{text:.2s}',
                textposition='outside',
            )

            st.plotly_chart(fig)
        else:
            st.write("Nenhum projeto realizado no último ano.")
