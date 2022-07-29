class SmartPhone:
    def __init__(self, model):
        self.model = model
        self.apps = list()

    def add_app(self, app):
        if len(tuple(filter(lambda x: type(x) == type(app), self.apps))) == 0:
            self.apps.append(app)

    def remove_app(self, app):
        self.apps.remove(app)



class AppVK:
    def __init__(self):
        self.name = "ВКонтакте"

class YouTube:
    def __init__(self, memory_max):
        self.name = "YouTube"
        self.memory_max = memory_max

class AppPhone:
    def __init__(self, contacts):
        self.name = "Phone"
        self.contacts = contacts
        self.phone_list = list()


video = YouTube(1011)
vk = AppVK()

mobi = SmartPhone("Cum")
mobi.add_app(video)
mobi.add_app(vk)
print(mobi.__dict__)
mobi.remove_app(vk)
print()
print(mobi.__dict__)
