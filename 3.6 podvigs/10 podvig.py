class Descr:
    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name, None)

    def __set__(self, instance, value):
        if type(value) not in (int, float) or value <= 0:
            raise ValueError("длины сторон треугольника должны быть положительными числами")
        setattr(instance,  self.name, value)

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __setattr__(self, key, value):
        if (key == "a" and not self.__check_triangle(value, self.b, self.c)) or \
                (key == "b" and not self.__check_triangle(value, self.a, self.c)) or \
                (key == "c" and not self.__check_triangle(value, self.a, self.b)):
            raise ValueError("с указанными длинами нельзя образовать треугольник")
        super().__setattr__(key, value)

    @staticmethod
    def __check_triangle(a, b, c):
        if a and b and c:
            return a < b + c and b < a + c and c < a + b

    def __len__(self):
        perim = int(self.a + self.b + self.c)
        return perim

    def __call__(self, *args, **kwargs):
        p = (self.a + self.b + self.c) // 2
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5