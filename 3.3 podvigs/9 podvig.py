class Recipe:
    def __init__(self, *args):
        self.ings = [*args]

    def add_ingredient(self, ing):
        if isinstance(ing, Ingredient):
            self.ings.append(ing)

    def remove_ingredient(self, ing):
        if isinstance(ing, Ingredient):
            self.ings.remove(ing)

    def get_ingredients(self):
        return tuple(self.ings)

    def __len__(self):
        return len(self.ings)


class Ingredient:
    def __init__(self, name, volume, measure):
        if type(name) == str:
            self.__name = name

        if type(volume) in (float, int):
            self.__volume = volume

        if type(measure) == str:
            self.__measure = measure

    def __str__(self):
        return f"{self.__name}, {self.__volume}, {self.__measure}"

rec = Recipe(Ingredient("Salt", 20, "fork"), Ingredient("Salt", 20, "fork"))
print(rec.get_ingredients())
print(len(rec))
