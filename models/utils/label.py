# Interfaces de Modelos (Meta Models)
from models.utils.db_session import DataBase


class Model(object):
    # Model object

    def __init__(self):
        self.session = DataBase()

    def __getattr__(self, attr):
        # Lazy Attr to models
        valur = attr
        setattr(self, attr, valur)
        return valur
