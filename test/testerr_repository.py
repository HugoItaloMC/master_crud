from threading import Lock

from tests_model.testerr_model import Product


class Descriptor:
    def __getattr__(self, item):
        value = item
        setattr(self, item, value)
        return value

    def method(self):
        raise NotImplementedError


class Api(Descriptor):

    def __init__(self):
        self.__produce = Product()
        self.lock = Lock()

    def __getattr__(self, item):
        return super().__getattr__(item)

    def method(self, require):
        with self.lock:
            data = require
            self.__produce.create_table()
            self.__produce.fname = data.get('fname')
            self.__produce.lname = data.get('lname')
            self.__produce.size = int(data.get('size'))
            self.__produce.poster()
