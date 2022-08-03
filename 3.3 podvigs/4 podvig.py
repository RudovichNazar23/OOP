import string

class WordString:
    def __init__(self, string=""):
        self.__string = string

    def __check_space(self):
        return True in [c in self.__string for c in string.whitespace]

    @property
    def string(self):
        return self.__string

    @string.setter
    def string(self, nw_str):
        if type(nw_str) == str:
            self.__string = nw_str
        else:
            raise TypeError("value must be str")

    def __len__(self):
        pass

    def words(self, indx):
        pass

words = WordString("Hello me")
words.string = "None"
print(words.__dict__)