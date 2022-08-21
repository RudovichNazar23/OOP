class DataBase:
    dict_db = {}

    def __init__(self, path):
        self.path = path

    def write(self, record):
        pass

    def read(self, pk):
        pass


class Record:
    __pk = 0

    @classmethod
    def __new__(cls, *args, **kwargs):
        cls.__pk += 1
        obj = super().__new__(cls)
        setattr(obj, 'id', cls.__pk)
        return obj

    def __init__(self, fio, descr, old):
        self.fio = fio
        self.descr = descr
        self.old = old

    def __hash__(self):
        pass


exp = Record("1", "1", 1)
print(exp.__dict__)

exp_2 = Record("2", "2", 2)
print(exp_2.__dict__)


