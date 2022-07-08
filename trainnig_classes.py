class Translator:
    def add(self, eng, rus):
        self.eng = eng
        self.rus = rus
        self.pare = {self.eng: self.rus}
        return self.pare

    def remove(self, eng):
        self.eng = eng
        del self.pare
        return True

    def translate(self, eng):
        self.eng = eng
        return self.pare[eng]


tr = Translator()

add_words = tr.add("tree", "дерево"), ("car",  "машина"), ("car", "автомобиль"), ("leaf", "лист"), ("river", "река"), ("go",  "идти"), ("go", "ехать"), ("go",  "ходить"), ("milk",  "молоко")

print(add_words)

print(tr.remove("car"))
print(tr.translate("go"))

