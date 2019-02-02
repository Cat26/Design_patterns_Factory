from .Chair import Chair


class Armchair(Chair):
    def __init__(self):
        super(Armchair, self).__init__()

    def config_furniture_type(self):
        self.type = 'armchair'
        self.making = 'white ecologic skin'
