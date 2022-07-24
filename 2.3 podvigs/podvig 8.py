class SuperShop:
    goods = list()

    def __init__(self, name):
        self.name = name

    def add_product(self, product):
        self.product = product
        self.goods.append(product)

    def remove_product(self, product):
        self.goods.remove(product)


class StringValue:
    def __init__(self, min_length=2, max_length=50):
        self.min_length = min_length
        self.max_length = max_length

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if type(value) == str and 2 < len(value) < 50:
            setattr(instance, self.name, value)

class PriceValue:
    def __init__(self, max_value=1000):
        if type(max_value) == int and 0 <= max_value <= 1000:
            self.max_value = max_value

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if type(value) == (int, float) and 0 <= value <= 1000:
            setattr(instance, self.name, value)

class Product:
    name = StringValue()
    price = PriceValue().max_value

    def __init__(self, name, price):
        self.name = name
        self.price = price

p = Product("milk", 20)
print(p.__dict__)

