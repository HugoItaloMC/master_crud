from abstract.single import Singleton
import sqlite3
from weakref import WeakKeyDictionary
# Configuracão com o banco de dados


class DataBase:
    _instance = {}

    def __new__(cls, database):
        if cls._instance is None:
            cls._instance[database] = super(DataBase, cls).__new__(cls)
            cls._instance[database].db = sqlite3.connect(database)
        return cls._instance[database]

    def disconect(self):
        if self.db is not None:
            self.db.close()
            self.db = None
            print("Closed Conexion")
        else:
            print("Dont connect anyway")

    def execute_query(self, query):
        if self.db is not None:
            cursor = self.db.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            cursor.close()
            return result
        else:
            print("Not query, state dont running")

if __name__ == '__main__':
    db1 = DataBase('storage.db')
    print(id(db1))
    db2 = DataBase('storage2.db')
    print(id(db2))
