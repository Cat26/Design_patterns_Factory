from AbstractFactory.Furniture import Furniture


class Chair(Furniture):
    def __init__(self):
        super(Chair, self).__init__()

    def config_furniture(self):
        self.name = 'chair'

