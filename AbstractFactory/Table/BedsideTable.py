from .Table import Table


class BedsideTable(Table):
    def __init__(self):
        super(BedsideTable, self).__init__()

    def config_furniture_type(self):
        self.type = 'bedside table'
        self.making = 'white wood'
