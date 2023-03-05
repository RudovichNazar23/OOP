class Singleton:
    obj = None

    def __new__(cls, *args, **kwargs):
        if cls.obj is None:
            cls.obj = super().__new__(cls)
        return cls.obj

    def __del__(self):
        Singleton.obj = None


class Game(Singleton):
    def __init__(self, name):
        if "name" not in self.__dict__:
            self.name = name
