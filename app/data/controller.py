"""Controller do Streamlit e banco de dados."""
from __future__ import annotations

from typing import TYPE_CHECKING

from models.projects import Projects
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

if TYPE_CHECKING:
    from datetime import datetime

# Configuração do Banco de Dados
DATABASE_URL = 'sqlite:///../database.db'
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

def get_projects(limit: int | None = None) -> list:
    """Retorna uma lista com todos os projetos,.

    limitando a quantidade se especificado.
    """
    with Session() as session:
        query = session.query(Projects)
        if limit:
            query = query.limit(limit)
        return query.all()

def get_top_5_projects_mais_receita(end_date: datetime) -> list:
    """Retorna os 5 projetos que geraram mais receita.

    até a data especificada.
    """
    with Session() as session:
        query = session.query(Projects).filter(Projects.end_date <= end_date)\
            .order_by(Projects.revenue.desc()).limit(5)
        return query.all()

def get_project_orcamento_excedente_por_semestre() -> dict:
    """Retorna a quantidade de projetos que excederam o orçamento."""
    with engine.connect() as conn:
        sql_query = text("""
        SELECT
            strftime('%Y', end_date) AS year,
            CASE
                WHEN strftime('%m', end_date) BETWEEN '01' AND '06' THEN '1st Semestre'
                WHEN strftime('%m', end_date) BETWEEN '07' AND '12' THEN '2nd Semestre'
            END AS Semestre,
            COUNT(*) AS total_projects,
            SUM(CASE WHEN project_cost > initial_budget THEN 1 ELSE 0 END) AS projetos_excedido_orçamento,
            (SUM(CASE WHEN project_cost > initial_budget THEN 1 ELSE 0 END) * 100.0 / COUNT(*)) AS porcentagem_excedido_orçamento
        FROM Projects
        WHERE end_date >= date('now', '-2 years')
        GROUP BY year, Semestre
        ORDER BY year, Semestre;
        """)
        result = conn.execute(sql_query)
        return result.fetchall()
