class Rect:
    def __init__(self, x, y, width, height):
        self.x, self.y = x, y
        self.width = width
        self.height = height

    def __eq__(self, other):
        if isinstance(other, Rect):
            return (self.width, self.height) == (other.width, other.height)

    def __hash__(self):
        return hash((self.width, self.height))