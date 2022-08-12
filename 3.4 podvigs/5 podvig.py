class ListMath:

    def __init__(self, lst=None):
        self.lst_math = lst[:] if lst and type(lst) == list else []

    @staticmethod
    def __check_type(value):
        return type(value) in (int, float)

    def __add__(self, other):
        if self.__check_type(other):
            self.lst_math = list(map(lambda x: x + other if type(x) in (int, float) and x > 0 else False,  self.lst_math))
            return self.lst_math

    def __radd__(self, other):
        if self.__check_type(other):
            return ListMath(list(map(lambda x: x + other if type(x) in (int, float) and x > 0 else False,  self.lst_math)))

    def __sub__(self, other):
        if self.__check_type(other):
            self.lst_math = list(map(lambda x: x - other if type(x) in (int, float) and x > 0 else False,  self.lst_math))
            return self.lst_math

    def __rsub__(self, other):
        if self.__check_type(other):
            return ListMath(list(map(lambda x: x - other if type(x) in (int, float) and x > 0 else False,  self.lst_math)))

    def __mul__(self, other):
        if self.__check_type(other):
            self.lst_math = list(map(lambda x: x * other if type(x) in (int, float) and x > 0 else False,  self.lst_math))
            return self.lst_math

    def __rmul__(self, other):
        if self.__check_type(other):
            return ListMath(list(map(lambda x: x * other if type(x) in (int, float) and x > 0 else False,  self.lst_math)))

    def __truediv__(self, other):
        if self.__check_type(other):
            self.lst_math = list(map(lambda x: x / other if type(x) in (int, float) and x > 0 else False,  self.lst_math))
            return self.lst_math

    def __rtruediv__(self, other):
        if self.__check_type(other):
            return ListMath(list(map(lambda x: x / other if type(x) in (int, float) and x > 0 else False,  self.lst_math)))


lst = [1, 2, 3, 4, 5]
exam = ListMath(lst)
exam += 2
print(exam.lst_math)



