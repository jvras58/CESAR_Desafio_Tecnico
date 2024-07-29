"""Sessão de conexão SqlAlchemy."""
from typing import Generator

from app.config.settings import Settings
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

engine = create_engine(Settings().DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_session() -> Generator[Session, None, None]:
    """Módulo para gerar uma sessão do banco de dados."""
    with SessionLocal() as session:
        yield session
