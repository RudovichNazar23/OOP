class StringText:
    def __init__(self, lst):
        self.lst = lst if type(lst) == list else None

    def __lt__(self, other):
        if isinstance(other, StringText):
            return len(str(self.lst).split()) < len(str(other.lst).split())

    def __le__(self, other):
        if isinstance(other, StringText):
            return len(str(self.lst).split()) <= len(str(other.lst).split())

    def __len__(self):
        return len(str(self.lst).split())


stich = ["Я к вам пишу – чего же боле?",
        "Что я могу еще сказать?",
        "Теперь, я знаю, в вашей воле",
        "Меня презреньем наказать.",
        "Но вы, к моей несчастной доле",
        "Хоть каплю жалости храня,",
        "Вы не оставите меня."]


lst_text = [StringText(string.strip('–?!,.;').split()) for string in stich]
lst_text_sorted = sorted(lst_text, key=lambda x: len(x))
lst_text_sorted = [' '.join(lst.lst) for lst in lst_text_sorted]

print(lst_text_sorted)


