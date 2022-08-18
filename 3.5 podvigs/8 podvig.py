class MoneyR:
    def __init__(self, cb=None, volume=None):
        self.__cb = cb
        self.__volume = volume

    @property
    def cb(self):
        return self.__cb

    @cb.setter
    def cb(self, volume):
        self.__cb = volume

    @property
    def volume(self):
        return self.__cb

    @volume.setter
    def volume(self, n_volume):
        self.__cb = n_volume

    def __lt__(self, other):
        if isinstance(other, (MoneyD, MoneyE)):
            if not CentralBank.register(other):
                raise ValueError("Неизвестен курс валют.")
        return (self.__cb, self.__volume) < (other.cb, other.volume)

    def __ge__(self, other):
        if isinstance(other, (MoneyD, MoneyE)):
            if not CentralBank.register(other):
                raise ValueError("Неизвестен курс валют.")
        return (self.__cb, self.__volume) < (other.cb, other.volume)

class MoneyD:
    def __init__(self, cb=None, volume=None):
        self.__cb = cb
        self.__volume = volume

    @property
    def cb(self):
        return self.__cb

    @cb.setter
    def cb(self, volume):
        self.__cb = volume

    @property
    def volume(self):
        return self.__cb

    @volume.setter
    def volume(self, n_volume):
        self.__cb = n_volume

    def __lt__(self, other):
        if isinstance(other, (MoneyR, MoneyE)):
            if not CentralBank.register(other):
                raise ValueError("Неизвестен курс валют.")
        return (self.__cb, self.__volume) < (other.cb, other.volume)

    def __ge__(self, other):
        if isinstance(other, (MoneyD, MoneyE)):
            if not CentralBank.register(other):
                raise ValueError("Неизвестен курс валют.")
        return (self.__cb, self.__volume) < (other.cb, other.volume)

class MoneyE:
    def __init__(self, cb=None, volume=None):
        self.__cb = cb
        self.__volume = volume

    @property
    def cb(self):
        return self.__cb

    @cb.setter
    def cb(self, volume):
        self.__cb = volume

    @property
    def volume(self):
        return self.__cb

    @volume.setter
    def volume(self, n_volume):
        self.__cb = n_volume

    def __lt__(self, other):
        if isinstance(other, (MoneyD, MoneyR)):
            if not CentralBank.register(other):
                raise ValueError("Неизвестен курс валют.")
        return (self.__cb, self.__volume) < (other.cb, other.volume)

    def __ge__(self, other):
        if isinstance(other, (MoneyD, MoneyE)):
            if not CentralBank.register(other):
                raise ValueError("Неизвестен курс валют.")
        return (self.__cb, self.__volume) < (other.cb, other.volume)


class CentralBank:
    def __init__(self):
        self.rates = {
            "rub": 72.5,
            "dollar": 1.0,
            "euro": 1.15
        }

    def __new__(cls, *args, **kwargs):
        if args:
            return None

    @classmethod
    def register(cls, money):
        if isinstance(money, (MoneyR, MoneyD, MoneyE)):
            return cls.__setattr__(money.cb)

