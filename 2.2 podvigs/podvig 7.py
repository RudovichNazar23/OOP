class RadiusVector2D:
    MIN_COORD = -100
    MAX_COORD = 1024

    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    @property
    def x_cor(self):
        print(self.__x)

    @x_cor.setter
    def x_cor(self, x):
        if type(x) == (int, float) and self.MIN_COORD <= x <= self.MAX_COORD:
            self.__x = x

    @property
    def y_cord(self):
        print(self.__y)

    @y_cord.setter
    def y_cord(self, y):
        if type(y) == (int, float) and self.MIN_COORD <= y <= self.MAX_COORD:
            self.__y = y

    @staticmethod
    def norm2(vector):
        pass

vector = RadiusVector2D(10, 20)
vector.x_cor = 25
vector.x_cor