from random import randint

class GamePole:
    __obj = None

    def __new__(cls, *args, **kwargs):
        if cls.__obj is None:
            cls.__obj = super().__new__(cls)
        return cls.__obj

    def __del__(self):
        GamePole.__obj = None

    def __init__(self, N, M, total_mines):
        self.N = N
        self.M = M
        self.total_mines = total_mines
        self.__pole_cells = None

    @property
    def pole_cells(self):
        return self.__pole_cells

    def init_pole(self):
        self.__pole_cells = (

        )

    def open_cell(self, i, j):
        pass

    def show_pole(self):
        pass


class Cell:
    def __init__(self):
        self.__is_mine = None
        self.__number = None
        self.__is_open = None

    @property
    def is_mine(self):
        return self.__is_mine

    @is_mine.setter
    def is_mine(self, value):
        if type(value) == bool:
            self.__is_mine = value
        else:
            raise ValueError("недопустимое значение атрибута")

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, value):
        if type(value) == int and 0 <= value <= 8:
            self.__number = value

    @property
    def is_open(self):
        return self.__is_open

    @is_open.setter
    def is_open(self, value):
        if type(value) == bool:
            self.__is_open = value

    def __bool__(self):
        return True if self.__is_open is False else False



