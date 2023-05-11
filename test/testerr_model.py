from test_db_session import DataBase

class Model:

    def __init__(self):
        self.dbset = DataBase()

    def __getattr__(self, item):
        value = item
        setattr(self, item, value)
        return value


class Product(Model):

    def __init__(self):
        super().__init__()

    def __getattr__(self, item):
        return super().__getattr__(item)

    def create_table(self):
        query = f'CREATE TABLE IF NOT EXISTS produto (id INTEGER PRIMARY KEY AUTOINCREMENT, fname TEXT, lname TEXT, size INTEGER)'
        self.dbset.execute_query(query)

    def post_table(self):
        query = 'INSERT INTO produto (fname, lname, size) VALUES(%s, %s, %s)' % (self.fname, self.lname, float(self.size))
        self.dbset.execute_query(query)

if __name__ == '__main__':
    produto = Product()
    produto.create_table()
