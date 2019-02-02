from AbstractFactory.Furniture import Furniture


class Table(Furniture):
    def __init__(self):
        super(Table, self).__init__()

    def config_furniture(self):
        self.name = 'table'
