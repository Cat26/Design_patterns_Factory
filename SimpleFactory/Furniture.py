from abc import ABCMeta, abstractmethod
from SimpleFactory.Singleton import Singleton


class Furniture(Singleton):
    __metaclass__ = ABCMeta

    @abstractmethod
    def config_details(self):
        pass