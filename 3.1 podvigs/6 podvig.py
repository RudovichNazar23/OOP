class Picture:
    def __init__(self, name, author, descr):
        self.name = name
        self.author = author
        self.descr = descr

class Mummies:
    def __init__(self, name, location, descr):
        self.name = name
        self.location = location
        self.descr = descr

class Papyri:
    def __init__(self, name, date, descr):
        self.name = name
        self.date = date
        self.descr = descr

class Museum:
    def __init__(self, name):
        self.name = name
        self.exhibits = list()

    def add_exhibit(self, obj):
        self.exhibits.append(obj.__dict__)

    def remove_exhibit(self, obj):
        if obj in self.exhibits:
            self.exhibits.remove(obj)

    def get_info_exhibit(self, indx):
        ex = self.exhibits[indx]
        print(f"Описание экспоната {ex.name}: {ex.descr}")

picture = Picture("Ja", "Ja", "Moja hujnia")
mummy = Mummies("Nazar", "Egypt", "New , fresh, yummy")


mus = Museum("Mienia")

mus.add_exhibit(picture)
mus.add_exhibit(mummy)

print(mus.__dict__)
print()

mus.get_info_exhibit(0)