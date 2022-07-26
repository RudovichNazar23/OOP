class TVProgram:
    def __init__(self, name):
        if type(name) == str:
            self.name = name
            self.items = list()
        else:
            raise TypeError("name must be STR ")

    def add_telecast(self, tl):
        self.items.append(tl)

    def remove_telecast(self, indx):
        for i in self.items:
            if i.uid == indx:
                self.items.remove(i)


class Telecast:
    def __init__(self, f_id, name, duration):
        if type(f_id) == int:
            self.__f_id = f_id

        if type(name) == str:
            self.__name = name

        if type(duration) == int:
            self.__duration = duration

    @property
    def uid(self):
        return self.__f_id

    @uid.setter
    def uid(self, new_id):
        if type(new_id) == int:
            self.__f_id = new_id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if type(new_name) == str:
            self.__name = new_name

    @property
    def duration(self):
        return self.__duration

    @duration.setter
    def duration(self, new_duration):
        if type(new_duration) == int:
            self.__duration = new_duration


tv = Telecast(1, "brazzers", 45)
print(tv.__dict__)

tv_chan = TVProgram("1_Channel")
tv_chan.add_telecast(tv)
print(tv_chan.__dict__.get("items"))
tv_chan.remove_telecast(1)
print()
print(tv_chan.__dict__.get("items"))

