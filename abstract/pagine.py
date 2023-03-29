
from abc import ABCMeta, abstractmethod


class APIMeta(metaclass=ABCMeta):
    # Interface API
    @abstractmethod
    def _post(self):
        (...)

    @abstractmethod
    def _put(self):
        (...)

    @abstractmethod
    def _remove(self):
        ...