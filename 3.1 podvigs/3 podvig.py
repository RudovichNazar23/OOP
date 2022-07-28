class Book:
    attrs = {
        "title": str,
        "author": str,
        "pages": int,
        "year": int
    }

    def __init__(self, title="", author="", pages=0, year=0):
        self.title = title
        self.author = author
        self.pages = pages
        self.year = year

    def __setattr__(self, key, value):
        if self.attrs[key] != type(value):
            raise TypeError("Неверный тип присваиваемых данных.")

        else:
            object.__setattr__(self, key, value)

book = Book("My history", "Nazar", 1000, 2020)
print(book.__dict__)