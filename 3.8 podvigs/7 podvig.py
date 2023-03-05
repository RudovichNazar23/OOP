class RadiusVector:
    def __init__(self, *args):
        self.coords = args

    def __getitem__(self, item):
        return self.coords[item]

    def __setitem__(self, key, value):
        self.coords = [*self.coords]
        self.coords[key] = value

