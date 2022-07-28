
class Shop:

    def __init__(self, name):
        self.name = name
        self.goods = list()

    def add_product(self, product):
        self.goods.append(product)

    def remove_product(self, product):
        if product in self.goods:
            self.goods.remove(product)
        else:
            print("There is not product like " + str(product))

class Product:
    __id = 0

    def __new__(cls, *args, **kwargs):
        cls.__id += 1
        obj = super().__new__(cls)
        setattr(obj, 'id', cls.__id)
        return obj

    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price

    def __setattr__(self, key, value):
        validate_type = {'id': isinstance(value, int),
                         'name': isinstance(value, str),
                         'weight': isinstance(value, (int, float)) and value > 0,
                         'price': isinstance(value, (int, float)) and value > 0}

        if validate_type[key]:
            return object.__setattr__(self, key, value)
        else:
            raise TypeError("Неверный тип присваиваемых данных.")

    def __delattr__(self, item):
        if item == 'id':
            raise AttributeError("Атрибут id удалять запрещено.")
        else:
            return object.__delattr__(self, item)
