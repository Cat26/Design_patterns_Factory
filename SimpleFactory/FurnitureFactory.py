from SimpleFactory.Chair.Armchair import Armchair
from SimpleFactory.Chair.KitchenChair import KitchenChair
from SimpleFactory.Table.BedsideTable import BedsideTable
from SimpleFactory.Table.Desk import Desk


class FurnitureFactory:
    def __init__(self):
        pass

    @staticmethod
    def create_furniture(type):

        if type == 'Armchair':
            furniture = Armchair()
        elif type == 'KitchenChair':
            furniture = KitchenChair()
        elif type == 'BedsideTable':
            furniture = BedsideTable()
        elif type == 'Desk':
            furniture = Desk()

        return furniture
