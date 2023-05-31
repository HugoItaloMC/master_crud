from abc import ABCMeta, abstractmethod

from models.model import Product


class APIMeta(metaclass=ABCMeta):

    def __init__(self):
        self.produce = Product()

    def __getattr__(self, attr):
        valur = attr
        setattr(self, attr, valur)
        return valur

    # Interface API

    @abstractmethod
    def post(self, *args):
        raise NotImplementedError

    @abstractmethod
    def put(self, *args):
        raise NotImplementedError

    @abstractmethod
    def remove(self, *args):
        raise NotImplementedError

    @abstractmethod
    def getall(self, *args):
        raise NotImplementedError
    
    @abstractmethod
    def getter(self, *args):
        raise NotImplementedError
