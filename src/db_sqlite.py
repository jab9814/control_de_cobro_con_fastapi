from fastapi import Depends, FastAPI
from typing import Annotated
from sqlmodel import SQLModel, Session, create_engine
from config_db import get_database_url, settings


engine = create_engine(
    get_database_url(), 
    connect_args=(
        {"check_same_thread": False} 
        if settings.db_engine == "sqlite" 
        else {}
    )
)


def create_all_tables(app: FastAPI):
    SQLModel.metadata.create_all(engine)
    yield


def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]