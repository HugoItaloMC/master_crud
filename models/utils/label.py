# Interfaces de Modelos (Meta Models)
from models.utils.db_session import DataBase



class Model(object):
    def __getattr__(self, item):
        # Lazy attr
        value = item
        setattr(self, item, value)
        return value

    def __init__(self):
        self.__db = DataBase()

    @property
    def session(self):
        return self.__db

    @session.setter
    def session(self, query):
        self.session(query)

