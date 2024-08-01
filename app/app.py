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
from streamlit.runtime.caching import cache_data

# Título do dashboard
st.title('Dashboard do CESAR - Desafio Técnico')


# Configuração da conexão com o banco de dados
DATABASE_URL = 'sqlite:///../database.db'
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

@cache_data
def get_projects(limit: int | None = None) -> list:
    """Retorna uma lista com todos os projetos,.

    limitando a quantidade se especificado.
    """
    with Session() as session:
        query = session.query(Projects)
        if limit:
            query = query.limit(limit)
        return query.all()

@cache_data
def get_top_5_projects_mais_receita(end_date: datetime) -> list:
    """Retorna os 5 projetos que geraram mais receita.

    até a data especificada.
    """
    with Session() as session:
        query = session.query(Projects).filter(Projects.end_date <= end_date)\
            .order_by(Projects.revenue.desc()).limit(5)
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
projects = get_projects(50)

# Exibir feedback interativo
with st.spinner('Carregando dados dos projetos...'):
    st.title("Rentabilidade líquida de cada projeto realizado no último ano.")
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
            margin={'t': 50, 'b': 150, 'l': 50, 'r': 50},
            height=600,
        )

        # Adicionando cores diferentes para cada barra
        fig.update_traces(marker_color=px.colors.qualitative.Plotly,
                        texttemplate='%{text:.2s}',
                        textposition='outside')

        # Exibir gráfico
        st.plotly_chart(fig)
    else:
        st.write("Nenhum projeto realizado no último ano.")

# Ler o conteúdo do arquivo SQL
with Path('/workspace/scripts/rentabilidade_liquida.sql').open() as file:
    rentabilidade_liquida_sql = file.read()

# Exibir a consulta SQL abaixo do gráfico
st.markdown("### Consulta SQL")
st.code(rentabilidade_liquida_sql, language='sql')

# Exibi gráfico dos 5 proj > receita até o final do segundo trimestre de 2024
final_2024_2_trimestre = datetime(2024, 6, 30, tzinfo=pytz.utc)
top_5_projects = get_top_5_projects_mais_receita(final_2024_2_trimestre)

if top_5_projects:
    top_5_projects_df = pd.DataFrame(
        [{'nome': p.project_name,
        'Receita': p.revenue,
        } for p in top_5_projects],
        )
    st.title("Dados dos 5 projetos com maior receita até o final de 2024:")
    st.write(top_5_projects_df)
    fig_top_5 = px.bar(
        top_5_projects_df,
        y='nome',
        x='Receita',
        orientation='h',
        title='Top 5 Projetos por Receita até o Final de 2024',
        text='Receita',
    )

    fig_top_5.update_layout(
        xaxis_title='Receita',
        yaxis_title='Nome do Projeto',
        title='Top 5 Projetos por Receita até o Final de 2024',
        font={'size': 14},
    )

    fig_top_5.update_traces(marker_color=px.colors.qualitative.Plotly,
                            texttemplate='%{text:.2s}',
                            textposition='outside')

    st.plotly_chart(fig_top_5)
else:
    st.write("Nenhum projeto com receita até o final de 2024.")

# Ler o conteúdo do arquivo SQL
with Path('/workspace/scripts/mais_receita_2_semestre_2024.sql').open() as file:
    mais_receita_2_semestre = file.read()

# Exibir a consulta SQL abaixo do gráfico
st.markdown("### Consulta SQL")
st.code(mais_receita_2_semestre, language='sql')
