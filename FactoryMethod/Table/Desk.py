from .TableFactory import TableFactory


class Desk(TableFactory):
    def __init__(self):
        super(Desk, self).__init__()

    def config_table_type(self):
        self.type = 'desk'
        self.making = 'solid black wood'