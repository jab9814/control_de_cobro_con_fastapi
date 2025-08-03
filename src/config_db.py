from pydantic_settings import BaseSettings
from pathlib import Path


class Settings(BaseSettings):
    db_engine: str
    db_host: str | None = None
    db_port: int | None = None
    db_user: str | None = None
    db_password: str | None = None
    db_name: str | None = None
    db_sqlite_path: str | None = None

    class Config:
        env_file = ".env"

settings = Settings()

def get_database_url() -> str:
    if settings.db_engine == "sqlite":
        db_path = Path(settings.db_sqlite_path).resolve()
        return f"sqlite:///{db_path}"
    
    if settings.db_engine == "postgresql":
        return (
            f"postgresql://{settings.db_user}:{settings.db_password}"
            f"@{settings.db_host}:{settings.db_port}/{settings.db_name}"
        )
    
    if settings.db_engine == "mysql":
        return (
            f"mysql+pymysql://{settings.db_user}:{settings.db_password}"
            f"@{settings.db_host}:{settings.db_port}/{settings.db_name}"
        )

    raise ValueError(f"Unsupported DB engine: {settings.db_engine}")
