from FactoryMethod.Chair.Armchair import Armchair
from FactoryMethod.Chair.KitchenChair import KitchenChair
from FactoryMethod.Table.BedsideTable import BedsideTable
from FactoryMethod.Table.Desk import Desk
from FactoryMethod.Wardrobe.DeskCabinet import DeskCabinet
from FactoryMethod.Wardrobe.WardrobeClothes import WardrobeClothes

if __name__ == '__main__':
    armchair = Armchair()
    print(armchair)

    armchair2 = Armchair()
    print(armchair2)

    c = KitchenChair()
    print(c)

    g = BedsideTable()
    print(g)

    f = DeskCabinet()
    print(f)

    t = WardrobeClothes()
    print(t)

    h = Desk()
    print(h)


