class Track:
    def __init__(self, start_x, start_y):
        self.start_x = start_x
        self.start_y = start_y
        self.trs = []

    @classmethod
    def belong(cls, other):
        return isinstance(other, TrackLine)

    def add_track(self, tr):
        if self.belong(tr):
            self.trs.append(tr)

    def get_tracks(self):
        return tuple(self.trs)

    def __eq__(self, other):
        pass

    def __lt__(self, other):
        pass

    def __len__(self):
        pass

class TrackLine:
    def __init__(self, to_x, to_y, max_speed):
        self.to_x = to_x
        self.to_y = to_y
        self.max_speed = max_speed


