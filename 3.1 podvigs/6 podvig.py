class Picture:
    def __init__(self, name, author, descr):
        self.name = name
        self.author = author
        self.descr = descr

    def __setattr__(self, key, value):
        attrs = {
            "name": isinstance(value, str),
            "author": isinstance(value, str),
            "descr": isinstance(value, str)
        }

        if attrs[key]:
            return object.__setattr__(self, key, value)
        else:
            raise TypeError("Неверный тип присваиваемых данных.")

class Mummies:
    def __init__(self, name, location, descr):
        self.name = name
        self.location = location
        self.descr = descr

    def __setattr__(self, key, value):
        attrs = {
            "name": isinstance(value, str),
            "location": isinstance(value, str),
            "descr": isinstance(value, str)
        }

        if attrs[key]:
            return object.__setattr__(self, key, value)
        else:
            raise TypeError("Неверный тип присваиваемых данных.")

class Papyri:
    def __init__(self, name, date, descr):
        self.name = name
        self.date = date
        self.descr = descr

    def __setattr__(self, key, value):
        attrs = {
            "name": isinstance(value, str),
            "date": isinstance(value, str),
            "descr": isinstance(value, str)
        }

        if attrs[key]:
            return object.__setattr__(self, key, value)
        else:
            raise TypeError("Неверный тип присваиваемых данных.")

class Museum:
    def __init__(self, name):
        self.name = name
        self.exhibits = list()

    def add_exhibit(self, obj):
        self.exhibits.append(obj.__dict__)

    def remove_exhibit(self, obj):
        self.exhibits.remove(obj)

    def get_info_exhibit(self, indx):
        for i in self.exhibits:
            if self.exhibits.index(i) == indx:
                return f"{i.__dict__[i.name]} : {i.__dict__[i.desc]}"

picture = Picture("Ja", "Ja", "Moja hujnia")
mus = Museum("Mienia")
mus.add_exhibit(picture)
print(mus.__dict__)
print()
print(mus.get_info_exhibit(0))