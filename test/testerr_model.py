from test_db_session import DataBase

class Model:

    def __init__(self):
        self.dbset = DataBase()

    def __getattr__(self, item):
        # Descriptor protocol for object
        value = item
        setattr(self, item, value)
        return value


class Product(Model):

    def __init__(self):
        super().__init__()
        self.db = self.dbset.db
        self.cursor = self.db.cursor()

    def __getattr__(self, item):
        return super().__getattr__(item)

    def create_table(self):
        query = f'CREATE TABLE IF NOT EXISTS produto (id INTEGER PRIMARY KEY AUTOINCREMENT, fname TEXT, lname TEXT, size INTEGER)'
        self.cursor.execute(query)
        self.cursor.fetchall()
        self.db.commit()
        self.db.close()


    def post_table(self):
        query = 'INSERT INTO produto (fname, lname, size) VALUES("%s", "%s", "%d")' % (self.fname, self.lname, int(self.size))
        self.cursor.execute(query)
        self.cursor.fetchall()
        self.db.commit()
        self.db.close()


if __name__ == '__main__':
    produto = Product()
    # Create Table
    #  produto.create_table()

    # Insert Into
    #  produto.fname = 'Adidas'
    #  produto.lname = 'Tênis'
    #  produto.size = '42'
    #  produto.post_table()

