from config.db_session import DataBase
# Interfaces de Modelos (Meta Models)

class Produto(object):

    def __init__(self, first_name: str, mind_name: str,
                 last_name: str, price: float, size: str):

        self.first_name: str = first_name
        self.mind_name: str = mind_name
        self.last_name: str = last_name
        self.price: float = price
        self.size: str = size
        # If not exists table from `calcados` create on database
        query = 'CREATE TABLE IF NOT EXISTS produto (id INTEGER PRIMARY KEY AUTOINCREMENT, first_name TEXT, mind_name TEXT, last_name TEXT, price REAL, size TEXT)'
        DataBase.session(query)
