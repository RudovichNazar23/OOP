class PolyLine:
    def __init__(self, *args):
        self.tup = [*args]

    def add_coord(self, x, y):
        if type(x) and type(y) is int:
            self.tup.append((x, y))

    def remove_coord(self, indx):
        self.tup.pop(indx)

    def get_coords(self):
        return self.tup

exp = PolyLine((1, 2), (3, 4))
exp.remove_coord(1)
exp.add_coord(3, 4)
print(exp.get_coords())
