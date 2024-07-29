"""Sessão de conexão SqlAlchemy."""
from typing import Generator

from app.config.settings import Settings
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

engine = create_engine(Settings().DATABASE_URL)


def get_session() -> Generator[Session, None, None]:
    """Módulo para gerar uma sessão do banco de dados."""
    with Session(engine) as session:
        yield session

