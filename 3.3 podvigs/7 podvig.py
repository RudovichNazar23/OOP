class RadiusVector:

    def __init__(self, arg1, *args):
        if len(args) == 1:
            self.__coords = [0] * arg1
        else:
            self.__coords = [arg1] + list(args)

    def set_coords(self, *args):
        n = len(args), len(self.__coords)
        self.__coords[:n] = args

    def get_coords(self):
        return tuple(self.__coords)

    def __len__(self):
        return len(self.__coords)

    def __abs__(self):
        return abs(sum([x**2 for x in self.__coords]) ** 0.5)


vector3D = RadiusVector(3)
vector3D.set_coords(3, -5.6, 8)
a, b, c = vector3D.get_coords()
vector3D.set_coords(3, -5.6, 8, 10, 11)
vector3D.set_coords(1, 2)
res_len = len(vector3D)
res_abs = abs(vector3D)
