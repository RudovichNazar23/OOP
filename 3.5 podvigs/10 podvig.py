class Box:
    def __init__(self):
        self.thg_lst = []

    def add_thing(self, obj):
        if isinstance(obj, Thing):
            self.thg_lst.append(obj.__dict__)

    def get_things(self):
        return self.thg_lst

    def __eq__(self, other):
        if isinstance(other, Box):
            return all(i in other.get_things() for i in self.get_things())

class Thing:
    def __init__(self, name, mass):
        self.name = name
        self.mass = mass

    def __eq__(self, other):
        if isinstance(other, Thing):
            return (self.mass, self.name.lower()) == (other.mass, other.name.lower())

