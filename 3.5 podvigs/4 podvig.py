class Dimensions:
    MIN_DIMENSION = 10
    MAX_DIMENSION = 10000

    @classmethod
    def __range(cls, attr):
        return cls.MIN_DIMENSION <= attr <= cls.MAX_DIMENSION

    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, value):
        if self.__range(value):
            self.__a = value
        else:
            return self.a

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, value):
        if self.__range(value):
            self.__b = value
        else:
            return self.b

    @property
    def c(self):
        return self.__c

    @c.setter
    def c(self, value):
        if self.__range(value):
            self.__c = value
        else:
            return self.c

    def __le__(self, other):
        if isinstance(other, Dimensions):
            return (self.__a, self.__b, self.__c) <= (other.__a, other.__b, other.__c)

    def __lt__(self, other):
        if isinstance(other, Dimensions):
            return (self.__a, self.__b, self.__c) <= (other.__a, other.__b, other.__c)


class ShopItem:
    def __init__(self, name, price, dim):
        self.name = name if isinstance(name, str) else None
        self.price = price if isinstance(price, (int, float)) else None
        self.dim = dim if isinstance(dim, Dimensions) else None


trainers = ShopItem('кеды', 1024, Dimensions(40, 30, 120))
umbrella = ShopItem('зонт', 500.24, Dimensions(10, 20, 50))
fridge = ShopItem('холодильник', 40000, Dimensions(2000, 600, 500))
chair = ShopItem('табуретка', 2000.99, Dimensions(500, 200, 200))
lst_shop = (trainers, umbrella, fridge, chair)
lst_shop_sorted = sorted(lst_shop, key=lambda x: x.dim)

print(lst_shop_sorted)


