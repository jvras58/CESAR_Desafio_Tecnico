"""Controller dos graficos."""
from __future__ import annotations

from typing import TYPE_CHECKING

from models.projects import Projects
from sqlalchemy import create_engine
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
