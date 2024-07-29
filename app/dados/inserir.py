"""Inserção de dados no banco de dados."""
from contextlib import contextmanager
from typing import Generator

from app.dados.projects_faker import generate_project_data
from app.database.session import get_session
from app.models.projects import Projects
from sqlalchemy.orm import Session


@contextmanager
def get_context_session() -> Generator[Session, None, None]:
    """Gerenciador de contexto para sessão do banco de dados."""
    session = get_session()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()

def project_50() -> list:
    """Cria 50 projetos."""
    with get_context_session() as session:
        projects_data = generate_project_data(50)
        projects = [Projects(**data) for data in projects_data]
        session.add_all(projects)
        return projects
