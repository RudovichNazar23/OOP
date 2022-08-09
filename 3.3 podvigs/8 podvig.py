class DeltaClock:
    def __init__(self, clock1, clock2):
        self.clock1 = clock1
        self.clock2 = clock2

    def __str__(self):
        res = self.__len__()
        h = res // 3600
        m = res % 3600 // 60
        s = res % 3600 % 60
        return f"{h:02}, {m:02}, {s:02}"

    def __len__(self):
        res = int(self.clock1.get_time()) - int(self.clock2.get_time())
        return res if res > 0 else 0


class Clock:

    def __check_values(self, value):
        return isinstance(value, int)

    def __init__(self, hours, minutes, seconds):
        if self.__check_values(hours):
            self.hours = hours
        else:
            self.hours = 0

        if self.__check_values(minutes):
            self.minutes = minutes
        else:
            self.minutes = 0

        if self.__check_values(seconds):
            self.seconds = seconds
        else:
            self.seconds = 0

    def get_time(self):
        return (self.hours * 3600) + (self.minutes * 60) + self.seconds


dt = DeltaClock(Clock(2, 15, 0), Clock(1, 30, 0))
print(dt)
len_dt = len(dt)
