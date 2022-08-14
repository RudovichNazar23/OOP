class Lib:
    def __init__(self):
        self.book_list = []

    def __add__(self, other):
        if isinstance(other, Book):
            self.book_list.append(other)
            return self

    def __iadd__(self, other):
        if isinstance(other, Book):
            self.book_list.append(other)
            return self

    def __sub__(self, other):
        if other in self.book_list:
            self.book_list.remove(other)
            return self

        elif type(other) == int:
            self.book_list.pop(other)
            return self

    def __isub__(self, other):
        if other in self.book_list:
            self.book_list.remove(other)
            return self

        elif type(other) == int:
            self.book_list.pop(other)
            return self

    def __len__(self):
        return len(self.book_list)

class Book:
    def __init__(self, title, author, year):
        if type(title) == str:
            self.title = title
        if type(author) == str:
            self.author = author
        if type(year) == int:
            self.year = year


book = Book("War and Peace", "Lion Tolstoy", 2020)
sec_book = Book("HI", "Ja", 2005)

lib = Lib()

lib += book
print(lib.__dict__)
