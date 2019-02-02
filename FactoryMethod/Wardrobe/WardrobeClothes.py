from .WardrobeFactory import WardrobeFactory


class WardrobeClothes(WardrobeFactory):
    def __init__(self):
        super(WardrobeClothes, self).__init__()

    def config_wardrobe_type(self):
        self.type = 'closet'
        self.making = 'solid black wood'