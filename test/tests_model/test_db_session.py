import sqlite3


class DataBase:
    # Settings to database
    def __getattr__(self, item):
        value = item
        setattr(self, item, value)
        return value

    def __call__(cls, *args, **kwargs):
        # To behaviours from singletons patterns in objects Python
        # Know here is writening from magic method `__call__`
        if not hasattr(cls, '_instance'):
            cls._instance = super(DataBase, cls).__call__(cls, *args, **kwargs)
        return cls._instance

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
    # Test isolated instances
    db1 = DataBase()
    print(id(db1))
    db2 = DataBase()
    print(id(db2))
