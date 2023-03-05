class Vector:
    _allowed_types = (int, float)

    def __init__(self, *args):
        self.__check_coords(args)
        self.args = args

    def __check_coords(self, coords):
        if not all(type(x) in self._allowed_types for x in coords):
            raise ValueError("неверный тип координат")

    def check_len(self, obj):
        if isinstance(obj, Vector):
            if not len(self.args) == len(obj.args):
                raise TypeError('размерности векторов не совпадают')

    def get_coords(self):
        return tuple(self.args)

    def __make_vector(self, coords):
        try:
            return self.__class__(*coords)
        except ValueError:
            return Vector(*coords)

    def __add__(self, other):
        self.check_len(other)
        result = tuple(i + j for i, j in zip(self.args, other.args))
        return self.__make_vector(result)

    def __sub__(self, other):
        self.check_len(other)
        result = tuple(i - j for i, j in zip(self.args, other.args))
        return self.__make_vector(result)


class VectorInt(Vector):
    _allowed_types = (int,)
