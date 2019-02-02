class Order(object):
    def __init__(self):
        self.ordered_furniture = []

    def add_furniture(self, new_furniture):
        self.ordered_furniture.append(new_furniture)

    def __str__(self):
        list = ''
        for el in self.ordered_furniture:
            list += str(el) + '\n'
        return list
