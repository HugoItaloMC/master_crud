import sqlite3

from config.single import Singleton


class DataBase(metaclass=Singleton):
    # Settings to database

    def __init__(self):
        self.dbset = sqlite3.connect('storage.db')

    def __call__(self, query):
        cursor = self.dbset.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        self.dbset.commit()
        return results[::1]

    def disconect(self):
        if self.dbset:
            self.dbset.close()
            self.dbset = None
            print("Close Conection")
        else:
            print("Dont connect anyway")

