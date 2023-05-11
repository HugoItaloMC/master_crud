from abstract.single import Singleton
import sqlite3
from weakref import WeakKeyDictionary
# Configuracão com o banco de dados


class DataBase:
    _instance = None

    def __call__(cls, *args, **kwargs):
        # To behaviours from singletons patterns in objects Python
        # Know here is writening from magic method `__call__`
        if cls._instance is None:
            cls._instance = super(DataBase, cls).__call__(cls, *args, **kwargs)
        return cls._instance

    def __getattr__(self, item):
        value = item  # Here let content know operation
        setattr(self, item, value)  # Create attr in object
        return value

    def create_db(self, database):
        if self._instance is None:
            self.db = sqlite3.connect(database)
        else:
            print("Run conection now !! ")

    def disconect(self):
        if self.db:
            self.db.close()
            self.db = None
            print("Close Conection")
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
    db1 = DataBase()
    db1.create_db('storage1.db')
    print(id(db1))
    db2 = DataBase()
    db2.create_db('storage2.db')
    print(id(db2))
