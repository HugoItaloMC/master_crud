from models.utils.label import Model


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

