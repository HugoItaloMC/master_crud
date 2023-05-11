from typing import Dict
from weakref import WeakKeyDictionary


class Singleton(type):

    # Controle de instâncias de objetos
    __instance = WeakKeyDictionary()

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instance:
            cls.__instance[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls.__instance[cls]
