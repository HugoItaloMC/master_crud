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

    def __init__(self):
        self.db = sqlite3.connect('storage.db')

    def disconect(self):
        if self.db:
            self.db.close()
            self.db = None
            print("Close Conection")
        else:
            print("Dont connect anyway")



if __name__ == '__main__':
    db1 = DataBase()
    db1.create_db('storage1.db')
    print(id(db1))
    db2 = DataBase()
    db2.create_db('storage2.db')
    print(id(db2))
