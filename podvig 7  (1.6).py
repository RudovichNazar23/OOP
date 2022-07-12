class SingletonFive:
    value = None
    count = 0

    def __new__(cls, *args, **kwargs):
        if cls.count < 5:
            cls.value = super().__new__(cls)
        cls.count += 1
        return cls.value

    def __init__(self, name):
        self.name = name


objs = [SingletonFive(str(n)) for n in range(10)]





