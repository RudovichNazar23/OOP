class Thing:
    id = 0

    def __new__(cls, *args, **kwargs):
        Thing.id += 1
        return object.__new__(cls)

    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.weight = self.dims = self.memory = self.frm = None
        self.id = self.id

    def get_data(self):
        return (self.id, self.name, self.price, self.weight, self.dims, self.memory, self.frm)


class Table(Thing):
    def __init__(self, name, price, weight, dims):
        super().__init__(name, price)
        self.weight = weight
        self.dims = dims

class ElBook(Thing):
    def __init__(self, name, price, memory, frm):
        super().__init__(name, price)
        self.memory = memory
        self.frm = frm
