class NewList:
    def __init__(self, lst=None):
        self.lst = lst[:] if lst and type(lst) == list else []
        self.res = None

    @staticmethod
    def __diff_elems(lst_1, lst_2):
        if len(lst_2) == 0:
            return lst_1

        sub = lst_2[:]
        return [x for x in lst_1 if not NewList.__compare_values(x, sub)]

    @staticmethod
    def __compare_values(var, sub):
        res = any(map(lambda q: type(var) == type(q) and q == var, sub))
        if res:
            sub.remove(var)
        return res

    def __sub__(self, other):
        if type(other) not in (list, NewList):
            raise ArithmeticError()
        oth_list = other if type(other) == list else other.get_list()
        return NewList(self.__diff_elems(self.lst, oth_list))

    def __rsub__(self, other):
        if type(other) != list:
            raise ArithmeticError()
        return NewList(self.__diff_elems(other, self.lst))

    def get_list(self):
        return self.lst


ex = NewList([1, 2, 3, 4])

lst = NewList
