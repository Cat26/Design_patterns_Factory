from .ChairFactory import ChairFactory


class KitchenChair(ChairFactory):
    def __init__(self):
        super(KitchenChair, self).__init__()

    def config_chair_type(self):
        self.type = 'kitchen chair'
        self.making = 'pine wood'