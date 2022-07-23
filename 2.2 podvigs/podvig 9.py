class LineTo:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class PathLines:
    def __init__(self, line):
        self.line = line

    def get_path(self):
        if LineTo:
            return list(self.line)
        else:
            return list()

    def get_length(self):
        return self.line.x + self.line.y

    def add_line(self):
        pass