from typing import Dict
from weakref import WeakKeyDictionary


class Singleton(type):

    # Controle de instâncias de objetos
    def __new__(meta, name, bases, class_dict):
        return type.__new__(meta, name, bases, class_dict)

    def __call__(cls, *args, **kwargs):
        if not hasattr(cls, '__instance'):
            cls.__instance = super(Singleton, cls).__call__(*args, **kwargs)
        return cls.__instance

