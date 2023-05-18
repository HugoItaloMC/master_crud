import sqlite3

from .test_db_session import DataBase


class Model:

    def __init__(self):
        self.session = DataBase()

    def __getattr__(self, item):
        # Descriptor protocol for object
        value = item
        setattr(self, item, value)
        return value


class Product(Model):

    def __init__(self):
        super().__init__()

    def __getattr__(self, item):
        return super().__getattr__(item)

    def create_table(self):
        query = f'CREATE TABLE IF NOT EXISTS produto (id INTEGER PRIMARY KEY AUTOINCREMENT, fname TEXT, lname TEXT, size INTEGER);'
        self.session.execute_query(query)

    def poster(self):
        query = 'INSERT INTO produto (fname, lname, size) VALUES("%s", "%s", "%d");' % (
            self.fname, self.lname, int(self.size))
        self.session.execute_query(query)

    def put(self, id: int):
        query = 'UPDATE produto SET fname = "%s", lname = "%s", size = "%d" WHERE id=%d;' % (
            self.fname, self.lname, int(self.size), id)
        self.session.execute_query(query)

    def getan(self):
        ...

    def geter(self):
        ...


    def delete(self, id):
        query = 'DELETE FROM produto WHERE id = "%d"' % id
        self.session.execute_query(query)


if __name__ == '__main__':
    produto = Product()
    # Test 1 Create Table : OK
    # produto.create_table()

    # Test 2 Post  : OK
    #produto.fname = 'Nike'
    #produto.lname = 'Tênis'
    #produto.size = '40'
    #produto.poster()

    #  Test 3 Put : OK
    # produto.fname = 'Adidas'
    # produto.lname = 'Camisa'
    # produto.size = '25'
    # produto.put(1)

    # Test 4 Delete : OK
    #  produto.delete(1)