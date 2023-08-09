import sqlalchemy as sa  # To DML
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.future.engine import Engine

from typing import Optional
from pathlib import Path  # to sqlite

from model_base import ModelBase  # Base models

__engine : Optional[Engine] = None


def create_engine(sqlite: bool = False) -> Engine:
    global __engine

    if __engine:
        #  Se já existir uma `engine` continuar ...
        return

    if sqlite:
        file_db = 'db/picoles.sqlite'
        path_db = Path(file_db).parent  # Criando arquivo dentro do diretório pai
        path_db.mkdir(parents=True, exist_ok=True)  #  `parents` Respeitando o diretório pai ; `exist_ok` se já existir ñ fazer nada

        str_engine = f"sqlite:///{path_db}"
        __engine = sa.create_engine(url=str_engine, echo=False, connect_args={"check_same_thread": False})  #  `connect_args` SqLite ñ trabalha com threads no sistema


    else:
        # To postgresql
        str_engine = "postgresql://postgres:Acesso93#@localhost:5432"
        __engine = sa.create_engine(url=str_engine, echo=False)

    return __engine


def create_session():

    if not __engine:
        create_engine()  # To sqlite `create_engine(sqlite=True)`

    __session = sessionmaker(__engine, expire_on_commit=False, class_=Session)

    session: Session = __session()
    return session


def create_tables() -> Session:

    global __engine

    if not __engine:
        create_engine()  # Case don't using postgresql `create_engine(sqlite=True)

    import __all_model
    ModelBase.metadata.drop_all(__engine)
    ModelBase.metadata.create_all(__engine)
