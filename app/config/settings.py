"""Configuração de variáveis de ambiente."""
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Configuração de variáveis de ambiente."""

    model_config = SettingsConfigDict(
        env_file='.env', env_file_encoding='utf-8',
    )

    DATABASE_URL: str
