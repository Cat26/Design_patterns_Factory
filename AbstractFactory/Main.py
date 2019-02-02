from AbstractFactory.Chair.KitchenChair import KitchenChair
from AbstractFactory.Chair.Armchair import Armchair
from AbstractFactory.Table.BedsideTable import BedsideTable
from AbstractFactory.Wardrobe.DeskCabinet import DeskCabinet
from AbstractFactory.Order import Order

if __name__ == '__main__':
    order = Order()

    furniture1 = Armchair()
    order.add_furniture(furniture1)

    furniture2 = KitchenChair()
    order.add_furniture(furniture2)

    furniture3 = BedsideTable()
    order.add_furniture(furniture3)

    furniture4 = DeskCabinet()
    order.add_furniture(furniture4)

    furniture5 = DeskCabinet()
    order.add_furniture(furniture5)

    print(order)
