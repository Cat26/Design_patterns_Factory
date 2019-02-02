from .WardrobeFactory import WardrobeFactory


class DeskCabinet(WardrobeFactory):
    def __init__(self):
        super(DeskCabinet, self).__init__()

    def config_wardrobe_type(self):
        self.type = 'desk cabinet'
        self.making = 'solid black wood'
