class Course:
    def __init__(self, name):
        self.name = name
        self.modules = list()

    def add_module(self, module):
        self.modules.append(module)

    def remove_module(self, indx):
        for i in self.modules:
            if self.modules.index(i) == indx:
                self.modules.remove(i)

    def __setattr__(self, key, value):
        attr = {
            "name": isinstance(value, str),
            "modules": isinstance(value, list)
        }
        if attr[key]:
            return object.__setattr__(self, key, value)
        else:
            TypeError("Неверный тип присваиваемых данных.")

    def __delattr__(self, item):
        if item == "modules":
            raise AttributeError(f"Атрибут {item} удалять запрещено.")


class Module:
    def __init__(self, name):
        self.name = name
        self.lessons = list()

    def __setattr__(self, key, value):
        attr = {
            "name": isinstance(value, str),
            "lessons": isinstance(value, list)
        }

        if attr[key]:
            return object.__setattr__(self, key, value)
        else:
            raise TypeError("Неверный тип присваиваемых данных.")

    def add_lesson(self, lesson):
        return self.lessons.append(lesson)

    def remove_lesson(self, indx):
        for i in self.lessons:
            if self.lessons.index(i) == indx:
                return self.lessons.remove(i)


class LessonItem:
    def __init__(self, title, practices, duration):
        self.title = title
        self.practices = practices
        self.duration = duration

    def __setattr__(self, key, value):
        validate_type = {'title': isinstance(value, str),
                         'practices': isinstance(value, (int, float)) and value > 0,
                         'duration': isinstance(value, (int, float)) and value > 0}

        if validate_type[key]:
            return object.__setattr__(self, key, value)
        else:
            raise TypeError("Неверный тип присваиваемых данных.")

    def __getattr__(self, item):
        if item:
            return False

    def __delattr__(self, item):
        if item:
            raise AttributeError(f"Атрибут {item} удалять запрещено.")
