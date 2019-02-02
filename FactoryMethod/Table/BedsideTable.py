from .TableFactory import TableFactory


class BedsideTable(TableFactory):
    def __init__(self):
        super(BedsideTable, self).__init__()

    def config_table_type(self):
        self.type = 'bedside table'
        self.making = 'white wood'