import sqlite3
from typing import Dict
from weakref import WeakKeyDictionary


class Singleton:

    # Controle de instâncias de objetos
    def __call__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__call__(cls)
        return cls.instance

    def __getattr__(self, item):
        value = item
        setattr(self, item, value)
        return value

if __name__ == '__main__':
    inst1 = Singleton()
    inst2 = Singleton()
    print(id(inst1),
          id(inst2))
    print(Singleton())