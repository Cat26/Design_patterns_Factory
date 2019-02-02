from .Wardrobe import Wardrobe


class DeskCabinet(Wardrobe):
    def __init__(self):
        super(DeskCabinet, self).__init__()

    def config_furniture_type(self):
        self.type = 'desk cabinet'
        self.making = 'solid black wood'