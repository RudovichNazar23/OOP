class IntegerValue:
    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if type(value) != int:
            raise ValueError('возможны только целочисленные значения')
        instance.__dict__[self.name] = value


class CellInteger:
    value = IntegerValue()

    def __init__(self, start_value=0):
        self.value = start_value

    def __call__(self, *args, **kwargs):
        return self


class TableValues:
    def __init__(self, rows, cols, cell):
        self.rows = rows
        self.cols = cols
        self.cell = cell
        self.cells = [[cell() for _ in range(cols)] for _ in range(rows)]

    def __setattr__(self, key, value):
        if key == "cell" and not bool(value):
            raise ValueError('параметр cell не указан')
        super().__setattr__(key, value)

    def __getitem__(self, ind):
        ind1, ind2 = ind[0], ind[1]
        return self.cells[ind1][ind2].value

    def __setitem__(self, key, value):
        ind1, ind2 = key[0], key[1]
        self.cells[ind1][ind2].value = value

