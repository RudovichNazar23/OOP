import sys

class Player:
    def __init__(self, name, old, score):
        self.name = name
        self.old = old
        self.score = score

    def __bool__(self):
        return True if self.score > 0 else False


lst_in = [
    "Балакирев; 34; 2048",
    "Mediel; 27; 0",
    "Влад; 18; 9012",
    "Nina P; 33; 0"
]
players = []

for var in lst_in:
    args = list(map(str.strip, var.split(";")))
    args[-1] = int(args[-1])
    obj = Player(*args)
    players.append(obj)

players_filtered = list(filter(lambda x: bool(x), players))
print(bool(players_filtered))


