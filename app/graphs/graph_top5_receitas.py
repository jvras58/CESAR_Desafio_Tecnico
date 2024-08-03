"""Exibe o conteúdo da página 5 Melhores Receitas."""
from datetime import datetime
from pathlib import Path

import pandas as pd
import plotly.express as px
import pytz
import streamlit as st
from data.controller import get_top_5_projects_mais_receita
from utils.utils import generate_colors


def top5_receitas_page() -> None:
    """Exibe a page 5 Melhores Receitas."""
    st.title("Top 5 Projetos por Receita")

    final_2024_2_trimestre = datetime(2024, 6, 30, tzinfo=pytz.utc)
    top_5_projects = get_top_5_projects_mais_receita(final_2024_2_trimestre)

    if top_5_projects:
        top_5_projects_df = pd.DataFrame(
            [{'nome': p.project_name, 'Receita': p.revenue} for p in top_5_projects],
        )
        with st.expander("Ver detalhes"):
            st.write("Dados dos 5 projetos com maior receita até o final de 2024:")
            st.write(top_5_projects_df)

        try:
            with Path('/workspace/scripts/mais_receita_2_semestre_2024.sql').open() as file:
                mais_receita_2_semestre = file.read()
        except FileNotFoundError:
                st.warning("Script SQL Somente aparece em desenvolvimento.")

        st.markdown("### Consulta SQL")
        st.code(mais_receita_2_semestre, language='sql')

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
            margin={'t': 50, 'b': 150, 'l': 50, 'r': 50},
            height=600,
            showlegend=False,
        )

        fig_top_5.update_traces(
            texttemplate='%{text:.2s}',
            textposition='outside',
        )

        st.plotly_chart(fig_top_5)
    else:
        st.write("Nenhum projeto com receita até o final de 2024.")
