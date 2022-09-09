class Ellipse:
    def __init__(self, *args):
        if args:
            self.x1, self.y1, self.x2, self.y2 = args

    def __bool__(self):
        return bool(self.__dict__)

    def get_coords(self):
        if self:
            return self.x1, self.y1, self.x2, self.y2
        else:
            raise AttributeError('нет координат для извлечения')


lst_geom = [Ellipse(), Ellipse(), Ellipse(), Ellipse()]

ex = Ellipse()
print(ex)

for obj in lst_geom:
    if bool(obj):
        print(obj.get_coords())