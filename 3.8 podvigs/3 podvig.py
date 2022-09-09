class Track:
    __lst = []

    def __init__(self, start_x, start_y):
        self.coord = start_x, start_y

    def add_point(self, x, y, speed):
        self.coord = (x, y), speed
        self.__lst.append(self.coord)

    def __getitem__(self, indx):
        if isinstance(indx, int) and 0 <= indx <= len(self.__lst):
            return self.__lst[indx]
        else:
            raise IndexError('некорректный индекс')

    def __setitem__(self, key, value):
        if isinstance(key, int) and 0 <= key <= len(self.__lst):
            self.__lst[key] = list(self.__lst[key])
            self.__lst[key][1] = value
            if self.__lst[key]:
                self.__lst[key] = tuple(self.__lst[key])
        else:
            raise IndexError('некорректный индекс')


