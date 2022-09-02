import sys

class DataBase:

    def __init__(self, path):
        self.path = path
        self.dict_db = {}


    def write(self, record):
        if isinstance(record, Record):
            self.dict_db.setdefault(record, [])
            self.dict_db[record].append(record)

    def read(self, pk):
        var = (x for row in self.dict_db.values() for x in row)
        obj = tuple(filter(lambda x: x.pk == pk, var))
        return obj[0] if len(obj) > 0 else None

class Record:
    pk = 0

    @classmethod
    def __new__(cls, *args, **kwargs):
        cls.pk += 1
        obj = super().__new__(cls)
        setattr(obj, 'id', cls.pk)
        return obj

    def __init__(self, fio, descr, old):
        self.fio = fio
        self.descr = descr
        self.old = old


    def __eq__(self, other):
        if isinstance(other, Record):
            return True if hash(self) == hash(other) else False


    def __hash__(self):
        return hash(self.fio.lower(), self.old)

db = DataBase("popa.db")

for i in lst_in:
    args = list(map(str.strip, i.split(":")))
    args[-1] = int(args[-1])
    db.write(Record(*args))

