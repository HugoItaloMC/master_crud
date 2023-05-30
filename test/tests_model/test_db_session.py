import sqlite3

from tests_model.test_single import Singleton


class DataBase(metaclass=Singleton):
    # Settings to database

    def __init__(self):
        self.dbset = sqlite3.connect('storage.db')

    def execute_query(self, query):
        cursor = self.dbset.cursor()
        cursor.execute(query)
        cursor.fetchall()
        self.dbset.commit()

    def disconect(self):
        if self.dbset:
            self.dbset.close()
            self.dbset = None
            print("Close Conection")
        else:
            print("Dont connect anyway")


if __name__ == '__main__':
    # Test isolated instances: `OK`
    db1 = DataBase()
    print(id(db1))
    db2 = DataBase()
    print(id(db2))
