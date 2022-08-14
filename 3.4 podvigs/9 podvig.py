class Box3D:
    def __init__(self, width, height, depth):
        self.width = width
        self.height = height
        self.depth = depth

    def __add__(self, other):
        if isinstance(other, Box3D):
            res = [self.width + other.width,
                   self.height + other.height,
                   self.depth + other.depth]

            return Box3D(*res)

    def __mul__(self, other):
        attrs = [
            self.width,
            self.height,
            self.depth
        ]
        if type(other) == int:
             attrs = [
                 self.width * other,
                 self.height * other,
                 self.depth * other
             ]
        return Box3D(*attrs)

    def __rmul__(self, other):
        attrs = [
            self.width,
            self.height,
            self.depth
        ]
        if type(other) == int:
            attrs = [
                self.width * other,
                self.height * other,
                self.depth * other,
            ]
        return Box3D(*attrs)

    def __sub__(self, other):
        if isinstance(other, Box3D):
            res = [
                self.width - other.width,
                self.height - other.height,
                self.depth - other.depth
            ]
            return Box3D(*res)

    def __floordiv__(self, other):
        attrs = [
            self.width,
            self.height,
            self.depth
        ]

        if type(other) == int:
            attrs = [
                self.width // other,
                self.height // other,
                self.depth // other,
            ]
        return Box3D(*attrs)

    def __mod__(self, other):
        attrs = [
            self.width,
            self.height,
            self.depth
        ]
        if type(other) == int:
            attrs = [
                self.width % other,
                self.height % other,
                self.depth % other,
            ]
        return Box3D(*attrs)

b_1 = Box3D(1, 2, 3)
b_2 = Box3D(4, 5, 6)

box = b_2 % 2

print(box.__dict__)

