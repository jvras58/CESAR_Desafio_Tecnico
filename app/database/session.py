"""Sessão de conexão SqlAlchemy."""

from app.config.settings import Settings
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

engine = create_engine(Settings().DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_session() -> Session:
    """Módulo para gerar uma sessão do banco de dados."""
    return SessionLocal()
