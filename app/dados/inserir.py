"""Inserção de dados no banco de dados."""
from contextlib import contextmanager
from typing import Generator

from app.dados.projects_factory import ProjectFactory
from app.database.session import (
    get_session,
)


@contextmanager
def get_context_session() -> Generator:
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
        ProjectFactory.reset_sequence()
        projects = ProjectFactory.build_batch(50)
        session.add_all(projects)
        return projects
