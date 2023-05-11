import sqlite3
from typing import Dict
from weakref import WeakKeyDictionary


class Singleton:

    # Controle de instâncias de objetos
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance


if __name__ == '__main__':
    inst1 = Singleton()
    inst2 = Singleton()
    print(id(inst1),
          id(inst2))
