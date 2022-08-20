class Body:
    def __init__(self, name, ro, volume):
        self.name = name
        self.ro = ro
        self.volume = volume

    def __lt__(self, other):
        if isinstance(other, Body):
            return (self.ro * self.volume) < (other.ro * other.volume)
        elif isinstance(other, (int, float)):
            return (self.ro * self.volume) < other

    def __eq__(self, other):
        if isinstance(other, Body):
            return (self.ro * self.volume) == (other.ro * other.volume)
        elif isinstance(other, (int, float)):
            return (self.ro * self.volume) == other

