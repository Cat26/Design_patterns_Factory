from SimpleFactory.FurnitureFactory import FurnitureFactory

if __name__ == '__main__':
    factory = FurnitureFactory()
    f = FurnitureFactory.create_furniture('Armchair')
    print(f.config_details())
    print(f)

    f2 = FurnitureFactory.create_furniture('Armchair')
    print(f2.config_details())
    print(f2)

    f3 = FurnitureFactory.create_furniture('KitchenChair')
    print(f3.config_details())
    print(f3)

    f4 = FurnitureFactory.create_furniture('Desk')
    print(f4.config_details())
    print(f4)
