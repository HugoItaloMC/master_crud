from abstract.label import Model


class Product(Model):
    # The product by model
    def __getattr__(self, attr):
        return super().__getattr__(attr)

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

    def getan(self, id: int):
        query = 'SELECT * FROM produto WHERE id="%d"' % id
        return self.session.execute_query(query)

    def geter(self):
        query = 'SELECT * FROM produto'
        return self.session.execute_query(query)

    def delete(self, id):
        query = 'DELETE FROM produto WHERE id="%d"' % id
        self.session.execute_query(query)


if __name__ == '__main__':

    produce = Product()
    print(produce.geter())
    print(produce.getan(1))
