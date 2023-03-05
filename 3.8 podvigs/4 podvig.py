class Array:
    def __init__(self, max_length, cell):
        self.max_length = max_length
        self.cell = cell
        self.array = [cell() for _ in range(self.max_length)]

    def __check_index(self, ind):
        if not isinstance(ind, int) or 0 > ind >= self.max_length:
            raise IndexError('неверный индекс для доступа к элементам массива')

    def __getitem__(self, ind):
        self.__check_index(ind)
        return self.array[ind].value

    def __str__(self):
        return " ".join(map(lambda x: str(x.value), self.array))

    def __setitem__(self, ind, value):
        self.__check_index(ind)
        self.array[ind].value = value


class Integer:
    def __init__(self, start_value=0):
        self.__value = start_value

    def __setattr__(self, key, value):
        if not type(value) == int:
            raise ValueError('должно быть целое число')
        return super().__setattr__(key, value)

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, n_val):
        if not type(n_val) == int:
            raise ValueError('должно быть целое число')
        self.__value = n_val
