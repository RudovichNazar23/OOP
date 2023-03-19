class Point:
    def __init__(self, x, y):
        self.set_coords(x, y)

    def set_coords(self, x, y):
        self.__x = x
        self.__y = y

    def get_coords(self):
        return self.__x, self.__y


class Rectangle:
    def __init__(self, *args):
        if len(args) == 2:
            self.set_coords(args[0], args[1])
        elif len(args) == 3:
            if type(args[0]) is int and type(args[1]) is int and type(args[2]) is Point:
                self.set_coords(Point(args[0], args[1]), args[2])
            elif type(args[0]) is Point and type(args[1]) is int and type(args[2]) is int:
                self.set_coords(args[0], Point(args[1], args[2]))
            else:
                raise TypeError('Incorrect data')
        elif len(args) >= 4:
            self.set_coords(Point(args[0], args[1]), Point(args[2], args[3]))
        else:
            raise Warning('Not enough data')

    def set_coords(self, sp, ep):
        self.__sp = sp
        self.__ep = ep

    def get_coords(self):
        return self.__sp, self.__ep

    def draw(self):
        print(f'Прямоугольник с координатами: {self.get_coords()[0].get_coords()} {self.get_coords()[1].get_coords()}')


rect = Rectangle(0, 0, 20, 34)

