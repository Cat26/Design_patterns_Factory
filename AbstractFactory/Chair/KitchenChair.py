from .Chair import Chair


class KitchenChair(Chair):
    def __init__(self):
        super(KitchenChair, self).__init__()

    def config_furniture_type(self):
        self.type = 'kitchen chair'
        self.making = 'pine wood'
