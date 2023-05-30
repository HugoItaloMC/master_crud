from abc import ABCMeta, abstractmethod


class APIMeta(metaclass=ABCMeta):
   
    def __getattr__(self, attr):
        valur = attr
        setattr(self, attr, valur)
        return valur

    # Interface API

    @abstractmethod
    def _post(self, *args):
        raise NotImplementedError

    @abstractmethod
    def _put(self, *args):
        raise NotImplementedError

    @abstractmethod
    def _remove(self, *args):
        raise NotImplementedError

    @abstractmethod
    def _getall(self, *args):
        raise NotImplementedError
    
    @abstractmethod
    def _get(self, *args):
        raise NotImplementedError
