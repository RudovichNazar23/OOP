class RadiusVector2D:
    MIN_COORD = -100
    MAX_COORD = 1024

    def __init__(self, x=0, y=0):
        if type(x) in (int, float) and self.MIN_COORD < x < self.MAX_COORD:
            self.__x = x
        else:
            self.__x = 0

        if type(y) in (int, float) and self.MIN_COORD < y < self.MAX_COORD:
            self.__y = y
        else:
            self.__y = 0

    @property
    def x_cor(self):
        return self.__x

    @x_cor.setter
    def x_cor(self, x):
        if type(x) in (int, float) and self.MIN_COORD <= x <= self.MAX_COORD:
            self.__x = x

    @property
    def y_cord(self):
        return self.__y

    @y_cord.setter
    def y_cord(self, y):
        if type(y) in (int, float) and self.MIN_COORD <= y <= self.MAX_COORD:
            self.__y = y

    @staticmethod
    def norm2(vector):
        return vector.__x ** 2 + vector.__y ** 2

