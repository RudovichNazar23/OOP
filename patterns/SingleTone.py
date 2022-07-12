class DataBase:
    object = None

    def __new__(cls, *args, **kwargs):
        if cls.object is None:
            cls.object = super().__new__(cls)

        return cls.object

    def __del__(self):
        DataBase.object = None

    def __int__(self, name, password):
        self.name = name
        self.password = password
