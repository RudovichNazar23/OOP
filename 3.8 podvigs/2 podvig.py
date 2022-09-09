class Record:
    __lst = []

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
        self.__add_keys()

    def __add_keys(self):
        for k in self.__dict__.keys():
            self.__lst.append(k)

    def __getitem__(self, item):
        if isinstance(item, int) and 0 <= item <= len(self.__lst):
            return self.__dict__[self.__lst[item]]
        else:
            raise IndexError('неверный индекс поля')

    def __setitem__(self, key, value):
        if isinstance(key, int) and 0 <= key <= len(self.__lst):
            self.__dict__[self.__lst[key]] = value