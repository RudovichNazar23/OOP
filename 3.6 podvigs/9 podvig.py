class Dimensions:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __setattr__(self, name, value):
        if value <= 0:
            raise ValueError("габаритные размеры должны быть положительными числами")
        object.__setattr__(self, name, value)

    def __hash__(self):
        return hash((self.a, self.b, self.c))

sp_inp = input()

"lst_dims = sorted(list(map(lambda x: hash(x), s_inp)), key=hash)"

exp = Dimensions(1, 2, 3)
print(exp.__dict__)