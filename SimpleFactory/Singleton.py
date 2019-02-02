from abc import ABCMeta, abstractmethod


class Singleton(object):
    __metaclass__ = ABCMeta

    instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.instance:
            cls.instance = super(Singleton, cls).__new__(
                cls, *args, **kwargs
            )
        return cls.instance

    @abstractmethod
    def config_furniture(self):
        pass

    @abstractmethod
    def config_furniture_type(self):
        pass