from interfaces.single import Singleton
import sqlite3

# Configuracão com o banco de dados


class DataBase(metaclass=Singleton):

    db = None

    def session(self, query):
        if self not in self.db:
            self.db = sqlite3.connect('./database.storage')
            self.cursor = self.db.cursor()
            try:
                self.cursor.execute(query)
                self.result = self.cursor.fetchall()
                self.db.commit()
            except Exception as err:
                raise f":: Error as {err} Try new query content now ##"
            finally:
                self.db.close()
        return DataBase.db()
