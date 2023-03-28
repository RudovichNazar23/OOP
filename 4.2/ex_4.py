class Thing:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    def __hash__(self):
        return hash((self.name, self.price, self.weight))


class DictShop(dict):
    def __init__(self, thing=None):
        thing = {} if thing is None else thing
        self.__check_type(thing)
        self.__check(thing)
        super().__init__(thing)

    @staticmethod
    def __check_type(thing):
        if not isinstance(thing, dict):
            raise TypeError('аргумент должен быть словарем')

    @staticmethod
    def __check(things):
        if not all(isinstance(key, Thing) for key in things):
            raise TypeError("ключами могут быть только объекты класса Thing")

    def __setitem__(self, key, value):
        if not isinstance(key, Thing):
            raise TypeError('ключами могут быть только объекты класса Thing')
        super().__setitem__(key, value)
