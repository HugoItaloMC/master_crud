import sqlite3

from tests_model_01.test_db_session import DataBase


class Model(object):

    @property
    def session(self):
        db = DataBase
        return db()

    @session.setter
    def session(self, query):
        self.session(query=query)

    def __getattr__(self, item):
        # Lazy attr
        value = item
        setattr(self, item, value)
        return value


class Product(Model):

    def __getattr__(self, item):
        return super().__getattr__(item)

    def create_table(self):
        query = f'CREATE TABLE IF NOT EXISTS produto (id INTEGER PRIMARY KEY AUTOINCREMENT, fname TEXT, lname TEXT, size INTEGER);'
        self.session(query)

    def poster(self):
        query = 'INSERT INTO produto (fname, lname, size) VALUES("%s", "%s", "%d");' % (
            self.fname, self.lname, float(self.size))
        self.session(query)

    def put(self, id: int):
        query = 'UPDATE produto SET fname = "{}", lname = "{}", size = "{}" WHERE id={};'.format(self.fname, self.lname, int(self.size), id)
        self.session(query)

    def getan(self, id: int):
        query = 'SELECT * FROM produto WHERE id="%d"' % int(id)
        return self.session(query)

    def geter(self):
        query = 'SELECT * FROM produto'
        return self.session(query)

    def delete(self, id):
        query = 'DELETE FROM produto WHERE id = "%d"' % id
        self.session(query)


if __name__ == '__main__':
    produto = Product()
    # Test 1 Create Table : OK
    #produto.create_table()

    # Test 2 Post  : OK
    #produto.fname = 'Nike'
    #produto.lname = 'Tênis'
    #produto.size = '40'
    #produto.poster()

    #  Test 3 Put : OK
    #produto.fname = 'Adidas'
    #produto.lname = 'Camisa'
    #produto.size = '25'
    #produto.put(1)

    # Test 4 Get All:
    #print(produto.geter())

    # Test 5 Get An:
    print(produto.getan(1))

    # Test 6 Delete : OK
    # produto.delete(1)
