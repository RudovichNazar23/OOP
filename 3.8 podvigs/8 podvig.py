class Cell:
    def __init__(self):
        self.value = 0
        self.is_free = True

    def __bool__(self):
        return bool(self.is_free)


class TicTacToe:
    def __init__(self):
        self.pole = tuple(tuple(Cell() for _ in range(3)) for _ in range(3))

    def clear(self):
        for row in self.pole:
            for cell in row:
                cell.value = 0
                cell.is_free = True

    def __check_item(self, item):
        if type(item) != tuple or len(item) != 2:
            raise IndexError('неверный индекс клетки')
        if any(not (0 <= 3) for x in item if type(x) != slice):
            raise IndexError('неверный индекс клетки')

    def __getitem__(self, item):
        self.__check_item(item)
        v, r = item
        if type(v) is slice:
            return tuple(self.pole[x][r].value for x in range(3))
        if type(r) is slice:
            return tuple(self.pole[v][x].value for x in range(3))
        return self.pole[v][r].value

    def __setitem__(self, key, value):
        self.__check_item(key)
        x, y = key
        if self.pole[x][y]:
            self.pole[x][y].value = value
            self.pole[x][y].is_free = False
        else:
            raise ValueError('клетка уже занята')