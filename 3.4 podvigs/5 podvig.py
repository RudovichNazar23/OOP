class ListMath:

    def __init__(self, lst=None):
        self.lst_math = lst if lst and type(lst) == list else []
        self.lst_math = list(filter(lambda x: type(x) in (int, float), self.lst_math))

    @staticmethod
    def __check_type(value):
        return type(value) in (int, float)

    def __add__(self, other):
        if self.__check_type(other):
            return ListMath([x + other for x in self.lst_math])

    def __radd__(self, other):
        if self.__check_type(other):
            return self + other

    def __sub__(self, other):
        if self.__check_type(other):
            return ListMath([x - other for x in self.lst_math])

    def __rsub__(self, other):
        if self.__check_type(other):
            return ListMath([other - x for x in self.lst_math])

    def __mul__(self, other):
        if self.__check_type(other):
            return ListMath([x * other for x in self.lst_math])

    def __rmul__(self, other):
        if self.__check_type(other):
            return self * other

    def __truediv__(self, other):
        if self.__check_type(other):
            return ListMath([x / other for x in self.lst_math])

    def __rtruediv__(self, other):
        if self.__check_type(other):
            return ListMath([x / other for x in self.lst_math])

    def __iadd__(self, other):
        if self.__check_type(other):
            self.lst_math = [x + other for x in self.lst_math]
            return self

    def __isub__(self, other):
        if self.__check_type(other):
            self.lst_math = [x - other for x in self.lst_math]
            return self

    def __imul__(self, other):
        if self.__check_type(other):
            self.lst_math = [x * other for x in self.lst_math]
            return self

    def __itruediv__(self, other):
        if self.__check_type(other):
            self.lst_math = [x / other for x in self.lst_math]
            return self


lst = [1, 2, 3, 4, 5]
exam = ListMath(lst)
res = exam + 2
print(exam.lst_math)



