from fastapi import Depends, FastAPI
from typing import Annotated
from sqlmodel import SQLModel, Session, create_engine


sqlite_name = '../data/db_project.sqlite3'
sqlite_url = f'sqlite:///{sqlite_name}'
engine = create_engine(url=sqlite_url)


def create_all_tables(app: FastAPI):
    SQLModel.metadata.create_all(engine)
    yield


def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]