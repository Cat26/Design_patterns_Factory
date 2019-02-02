from abc import ABCMeta, abstractmethod
from AbstractFactory.Singleton import Singleton


class Furniture(Singleton):
    __metaclass__ = ABCMeta

    def __init__(self):
        self.name = None
        self.type = None
        self.making = None

        self.config_furniture()
        self.config_furniture_type()

    @abstractmethod
    def config_furniture(self):
        pass

    @abstractmethod
    def config_furniture_type(self):
        pass

    def __str__(self):
        return 'furniture: {0} type: {1} details: {2}' \
            .format(self.name, self.type, self.making)
