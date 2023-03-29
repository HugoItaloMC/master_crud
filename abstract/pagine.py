
from abc import ABCMeta, abstractmethod

from config._2handler import Index

class APIMeta(Index, metaclass=ABCMeta):
   
    # Interface API
   
    @abstractmethod
    def _post(self):
        ...

    @abstractmethod
    def _put(self):
        ...

    @abstractmethod
    def _remove(self):
        ...

    @abstractmethod
    def _getall(self):
        ...
    
    @abstractmethod
    def _get(self):
        ...