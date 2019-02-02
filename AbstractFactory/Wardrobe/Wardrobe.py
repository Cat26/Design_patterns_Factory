from AbstractFactory.Furniture import Furniture


class Wardrobe(Furniture):
    def __init__(self):
        super(Wardrobe, self).__init__()

    def config_furniture(self):
        self.name = 'wardrobe'
