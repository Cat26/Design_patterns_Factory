from .Table import Table


class Desk(Table):
    def __init__(self):
        super(Desk, self).__init__()

    def config_furniture_type(self):
        self.type = 'desk'
        self.making = 'solid black wood'