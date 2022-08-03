class Model:
    def __init__(self):
        self.dct = None

    def query(self, **kwargs):
        self.dct = kwargs

    def __str__(self):
        if self.dct is not None:
            return "Model: " + ", ".join([f"{k} = {v}" for k, v in self.dct.items()])
        else:
            return "Model"

model = Model()
model.query(id=1, name="Nazar")
print(model)
