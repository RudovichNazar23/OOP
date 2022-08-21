import sys
from collections import Counter

class ShopItem:
    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price

    def __eq__(self, other):
        if self.__hash__(self):
            return hash(self) == hash(other)

    def __hash__(self):
        return hash((self.name, self.weight, self.price))


it_1 = ShopItem("Системный блок", 1500, 75890.56)
it_2 = ShopItem("Монитор Samsung", 2000, 34000)
it_3 = ShopItem("Клавиатура", 200.44, 545)
it_4 = ShopItem("Монитор Samsung", 2000, 34000)


lst = [
    it_1,
    it_2,
    it_3,
    it_4
]

lst_in = list(map(str.strip, sys.stdin.readlines()))

shop_items = {}
items = []
for line in lst_in:
    name, data = line.split(':')
    weight, price = map(float, data.split())
    items.append(ShopItem(name, weight, price))

shop_items = {k: [k, v] for k, v in Counter(items).items()}

