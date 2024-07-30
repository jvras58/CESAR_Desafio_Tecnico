"""Dashboard do CESAR - Desafio Técnico."""

from __future__ import annotations

from datetime import datetime, timedelta
from pathlib import Path

import pandas as pd
import plotly.express as px
import pytz
import streamlit as st
from models.projects import Projects
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Título do dashboard
st.title('Dashboard do CESAR - Desafio Técnico')

engine = create_engine('sqlite:///../database.db')
Session = sessionmaker(bind=engine)
session = Session()

def get_projects(limit: int | None = None) -> list:
    """Retorna uma lista com todos os projetos.

    limitando a quantidade se especificado.
    """
    query = session.query(Projects)
    if limit:
        query = query.limit(limit)
    return query.all()

def get_project_ultimo_ano(projects: list) -> list:
    """Filtra projetos realizados no último ano.

    e calcula a rentabilidade líquida.
    """
    utc_now = datetime.now(pytz.utc)
    one_year_ago = utc_now - timedelta(days=365)
    return [
        {
            'nome': project.project_name,
            'Rentabilidade_liquida': project.revenue - project.project_cost,
        }
        for project in projects
        if project.end_date.replace(tzinfo=pytz.utc) >= one_year_ago
    ]

# Buscar dados dos projetos
projects = get_projects(10)

st.write("Rentabilidade líquida de cada projeto realizado no último ano.")
st.write(f"Total de projetos retornados pelo Banco: {len(projects)}")

# Filtra projetos do último ano e calcular a rentabilidade líquida
project_ultimo_ano = get_project_ultimo_ano(projects)
st.write(f"Total de projetos do último ano: {len(project_ultimo_ano)}")

# Cria o gráfico de rentabilidade líquida
if project_ultimo_ano:
    projects_df = pd.DataFrame(project_ultimo_ano)
    st.write("Dados dos projetos do último ano:")
    st.write(projects_df)
    fig = px.bar(
        projects_df,
        x='nome',
        y='Rentabilidade_liquida',
        title='Rentabilidade Líquida dos Projetos do Último Ano',
        text='Rentabilidade_liquida',
    )

    # Atualizações de layout para melhorar a legibilidade
    fig.update_layout(
        xaxis_title='Nome do Projeto',
        yaxis_title='Rentabilidade Líquida',
        title='Rentabilidade Líquida dos Projetos do Último Ano',
        xaxis_tickangle=-45,
        font={'size': 14},
    )

    # Adicionando cores diferentes para cada barra
    fig.update_traces(marker_color=px.colors.qualitative.Plotly,
                    texttemplate='%{text:.2s}',
                    textposition='outside')

    # Exibi gráfico
    st.plotly_chart(fig)
else:
    st.write("Nenhum projeto realizado no último ano.")

# Le o conteúdo do arquivo SQL
with Path('/workspace/scripts/rentabilidade_liquida.sql').open() as file:
    rentabilidade_liquida_sql = file.read()

# Exibi a consulta SQL abaixo do gráfico
st.markdown("### Consulta SQL")
st.code(rentabilidade_liquida_sql, language='sql')



