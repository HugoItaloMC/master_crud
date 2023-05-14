import sqlite3


class DataBase:
    # Settings to database

    def __call__(cls, *args, **kwargs):
        # To behaviours from singletons patterns in objects Python
        # Know here is writening from magic method `__call__`
        if not hasattr(cls, '_instance'):
            cls._instance = super(DataBase, cls).__call__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        self.db = sqlite3.connect('storage.db')  # Create DB

    def execute_query(self, query):
        cursor = self.db.cursor()
        cursor.execute(query)
        cursor.fetchall()
        self.db.commit()
        self.db.close()


    def disconect(self):
        if self.db:
            self.db.close()
            self.db = None
            print("Close Conection")
        else:
            print("Dont connect anyway")



if __name__ == '__main__':
    # Test isolated instances
    db1 = DataBase()
    print(id(db1))
    db2 = DataBase()
    print(id(db2))
