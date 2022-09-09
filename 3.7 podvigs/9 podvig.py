from operator import sub, add, mul


class Vector:

    def __init__(self, *args):
        self.args = args

    @staticmethod
    def check_len(self, other):
        if not type(other) == int and len(self.args) != len(other.args):
            raise ArithmeticError('размерности векторов не совпадают')
        return True

    def __sub__(self, other):
        self.check_len(self, other)
        other = other.args if isinstance(other, Vector) else [other for i in range(other)]
        return Vector(*map(lambda x: sub(*x), zip(self.args, other)))

    def __add__(self, other):
        self.check_len(self, other)
        other = other.args if isinstance(other, Vector) else [other for i in range(other)]
        return Vector(*map(lambda x: add(*x), zip(self.args, other)))

    def __mul__(self, other):
        self.check_len(self, other)
        other = other.args if isinstance(other, Vector) else [other for i in range(other)]
        return Vector(*map(lambda x: mul(*x), zip(self.args, other)))

    def __eq__(self, other):
        return self.args == other.args