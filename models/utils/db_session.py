import sqlite3

from config import Singleton

# Configuracão com o banco de dados


class DataBase(metaclass=Singleton):
    # Settings to database:

    def __init__(self):
        self._dbset = sqlite3.connect('storage.db')

    def execute_query(self, query):
        cursor = self._dbset.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        self._dbset.commit()
        return results[::1]

    def disconect(self):
        if self._dbset:
            self._dbset.close()
            self._dbset = None
