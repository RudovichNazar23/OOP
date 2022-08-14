class Budget:

    def __init__(self):
        self.items_list = []

    def add_item(self, it):
        if isinstance(it, Item):
            self.items_list.append(it)

    def remove_item(self, indx):
        self.items_list.pop(indx)

    def get_items(self):
        return self.items_list


class Item:
    def __init__(self, name, money: (int, float)):
        self.name = name
        self.money = money

    def __add__(self, other):
        if isinstance(other, Item):
            return self.money + other.money

    def __radd__(self, other):
        if isinstance(other, (Item, int)):
            return self.money + other


it_1 = Item("1", 20)
it_2 = Item("2", 20)
it_3 = Item("3", 20)
it_4 = Item("4", 20)

res = it_1 + it_2 + it_3 + it_4
print(res)