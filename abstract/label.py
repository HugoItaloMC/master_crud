# Interfaces de Modelos (Meta Models)
from config.db_session import DataBase


class Model(object):
    # Model object

    def __init__(self):
        self.session = DataBase()

    def __getattr__(self, attr):
        # To insert attr in execution
        valur = attr
        setattr(self, attr, valur)
        return valur
