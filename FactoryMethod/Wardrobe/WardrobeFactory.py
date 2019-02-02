from FactoryMethod.Singleton import Singleton
from abc import ABCMeta, abstractmethod


class WardrobeFactory(Singleton):
    __metaclass__ = ABCMeta

    def __init__(self):
        self.name = 'wardrobe'
        self.type = None
        self.making = None

        self.config_wardrobe_type()

    @abstractmethod
    def config_wardrobe_type(self):
        pass

    def __str__(self):
        return 'furniture: {0} type: {1} details: {2}' \
            .format(self.name, self.type, self.making)