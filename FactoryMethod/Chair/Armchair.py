from FactoryMethod.Chair.ChairFactory import ChairFactory


class Armchair(ChairFactory):
    def __init__(self):
        super(Armchair, self).__init__()

    def config_chair_type(self):
        self.type = 'armchair'
        self.making = 'white ecologic skin'