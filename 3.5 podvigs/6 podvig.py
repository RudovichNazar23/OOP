class Morph:
    def __init__(self, *args):
        self.args = [*args]

    def add_word(self, word):
        wrd = word.lower()
        if wrd not in self.args:
            return self.args.append(word)

    def get_words(self):
        return tuple(self.args)

    def __eq__(self, other):
        return True if other.lower() in self.args else False

dict_words = [
        Morph("связь",  "связи",  "связью",  "связей",  "связям",  "связями",  "связях"),
        Morph("формула",  "формулы",  "формуле",  "формулу",  "формулой",  "формул",  "формулами", "формулах"),
        Morph("вектор",  "вектора",  "вектору",  "вектором",  "векторе",  "векторы",  "векторов", "векторам", "векторами", "векторах"),
        Morph("эффект", "эффекта", "эффекту", "эффектом", "эффекте", "эффекты", "эффектов", "эффектам", "эффектами", "эффектах"),
        Morph("день", "дня", "дню", "днем", "дне", "дни", "дням", "днями", "днях")
]

text = "Мы будем устанавливать связь завтра днем."

words = map(lambda x: x.strip("?!:;,.").lower(), text.split())

res = sum(word == morph for word in words for morph in dict_words)
print(res)
