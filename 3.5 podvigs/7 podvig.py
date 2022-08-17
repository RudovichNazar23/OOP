class FileAcceptor:
    def __init__(self, *args):
        self.files = [*args]

    def __call__(self, filename: str, **kwargs):
        return True if filename.split('.')[-1] in self.files else False

    def __add__(self, other):
        if isinstance(other, FileAcceptor):
            return FileAcceptor(*self.files + other.files)


ac = FileAcceptor("boat.jpg")
ac_2 = FileAcceptor("ww", "bmp")
print(ac("jpg"))

