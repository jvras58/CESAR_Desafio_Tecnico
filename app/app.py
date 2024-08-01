"""Dashboard do CESAR - Desafio Técnico."""

from __future__ import annotations

from datetime import datetime
from pathlib import Path

import pandas as pd
import plotly.express as px
import pytz
import streamlit as st
from dados.controller import get_projects, get_top_5_projects_mais_receita
from utils.utils import generate_colors, get_project_ultimo_ano

st.title('Dashboard do CESAR - Desafio Técnico')

# ----------------------------------
#  Limite de dados
# ----------------------------------
# Buscar dados dos projetos
projects = get_projects(50)

# ----------------------------------
#  Grafico de barras 1: Rentabilidade líquida
# ----------------------------------

with st.spinner('Carregando dados dos projetos...'):
    st.title("Rentabilidade líquida de cada projeto realizado no último ano.")
    st.write(f"Total de projetos retornados pelo Banco: {len(projects)}")

    project_ultimo_ano = get_project_ultimo_ano(projects)
    st.write(f"Total de projetos do último ano: {len(project_ultimo_ano)}")

    if project_ultimo_ano:
        projects_df = pd.DataFrame(project_ultimo_ano)
        st.write("Dados dos projetos do último ano:")
        st.write(projects_df)

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

with Path('/workspace/scripts/rentabilidade_liquida.sql').open() as file:
    rentabilidade_liquida_sql = file.read()

st.markdown("### Consulta SQL")
st.code(rentabilidade_liquida_sql, language='sql')

# ----------------------------------
#  Grafico de barras 2: + Receita TOP 5
# ----------------------------------

final_2024_2_trimestre = datetime(2024, 6, 30, tzinfo=pytz.utc)
top_5_projects = get_top_5_projects_mais_receita(final_2024_2_trimestre)

if top_5_projects:
    top_5_projects_df = pd.DataFrame(
    [{'nome': p.project_name, 'Receita': p.revenue} for p in top_5_projects],
    )
    st.title("Dados dos 5 projetos com maior receita até o final de 2024:")
    st.write(top_5_projects_df)

    colors = generate_colors(len(top_5_projects_df))

    fig_top_5 = px.bar(
        top_5_projects_df,
        y='nome',
        x='Receita',
        orientation='h',
        title='Top 5 Projetos por Receita até o Final de 2024',
        text='Receita',
        color='nome',
        color_discrete_sequence=colors,
    )

    fig_top_5.update_layout(
        xaxis_title='Receita',
        yaxis_title='Nome do Projeto',
        title='Top 5 Projetos por Receita até o Final de 2024',
        font={'size': 14},
        showlegend=False,
    )

    fig_top_5.update_traces(
        texttemplate='%{text:.2s}',
        textposition='outside',
    )

    st.plotly_chart(fig_top_5)
else:
    st.write("Nenhum projeto com receita até o final de 2024.")

with Path('/workspace/scripts/mais_receita_2_semestre_2024.sql').open() as file:
    mais_receita_2_semestre = file.read()

st.markdown("### Consulta SQL")
st.code(mais_receita_2_semestre, language='sql')
