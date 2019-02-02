from SimpleFactory.Furniture import Furniture


class Table(Furniture):

    def __init__(self):
        pass

    def config_details(self):
        return 'furniture:' + self.__class__.__name__