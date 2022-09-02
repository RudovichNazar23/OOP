class BookStudy:
    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = year

    def __eq__(self, other):
        if isinstance(other, BookStudy):
            return True if hash(self) == hash(other) else False

    def __hash__(self):
        return hash((self.name.lower(), self.author.lower()))


lst_in = [
    'Python; Балакирев С.М.; 2020',
    'Python ООП; Балакирев С.М.; 2021',
    'Python ООП; Балакирев С.М.; 2022',
    'Python; Балакирев С.М.; 2021',
]

lst_bs = []

unique_books = 0

for var in lst_in:
    name, author, year = var.split(";")
    obj = BookStudy(name, author, int(year))
    lst_bs.append(obj)
unique_books = len(set(lst_bs))

print(lst_bs, unique_books, sep="\n")


