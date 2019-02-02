from .Wardrobe import Wardrobe


class WardrobeClothes(Wardrobe):
    def __init__(self):
        super(WardrobeClothes, self).__init__()

    def config_furniture_type(self):
        self.type = 'closet'
        self.making = 'solid black wood'
