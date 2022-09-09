class Bag:
    def __init__(self, max_weight):
        self.max_weight = max_weight
        self.__bag = []

    def get_bag(self):
        return self.__bag

    def add_thing(self, thing):
        if isinstance(thing, Thing):
            if thing.weight < self.max_weight and len(self.__bag) == 0:
                self.__bag.append(thing)
            elif len(self.__bag) > 0 and self.__bag[-1].weight + thing.weight <= self.max_weight:
                self.__bag.append(thing)
            else:
                raise ValueError('превышен суммарный вес предметов')

    def __getitem__(self, item):
        if isinstance(item, int) and 0 <= item <= len(self.__bag):
            return self.__bag[item]
        else:
            raise IndexError('неверный индекс')

    def __setitem__(self, key, value):
        if isinstance(key, int) and 0 <= key <= len(self.__bag):
            self.__bag[key] = value
        else:
            raise IndexError('неверный индекс')

    def __delitem__(self, key):
        if isinstance(key, int) and 0 <= key <= len(self.__bag):
            del self.__bag[key]
        else:
            raise IndexError('неверный индекс')


class Thing:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight


thug_life = Thing("AK", 47)
thug_food = Thing("weed", 10)

thug_bag = Bag(100)
thug_bag.add_thing(thug_life)
thug_bag.add_thing(thug_food)
thug_bag[0] = Thing("Deagle", 500)
print(thug_bag.get_bag())






