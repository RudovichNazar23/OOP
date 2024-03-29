class Complex:
    def __init__(self, real, img):
        if type(real) in (int, float):
            self.__real = real
        else:
            raise ValueError("Неверный тип данных.")

        if type(img) in (int, float):
            self.__img = img
        else:
            raise ValueError("Неверный тип данных.")

    @property
    def real(self):
        return self.__real

    @real.setter
    def real(self, value):
        if type(value) in (int, float):
            self.__real = value
        else:
            raise ValueError("Неверный тип данных.")

    @property
    def img(self):
        return self.__img

    @img.setter
    def img(self, value):
        if type(value) in (int, float):
            self.__img = value
        else:
            raise ValueError("Неверный тип данных.")

    def __abs__(self):
        return (self.__real**2 + self.__img**2) ** 0.5

cmp = Complex(7, 8)
cmp.real = 3
cmp.img = 4
c_abs = abs(cmp)
print(c_abs)
