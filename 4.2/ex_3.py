class ListInteger(list):
    def __init__(self, lst):
        for x in lst:
            self.__check_type(x)
        super().__init__(lst)

    @staticmethod
    def __check_type(var):
        if not isinstance(var, int):
            raise TypeError('можно передавать только целочисленные значения')

    def __setitem__(self, key, value):
        self.__check_type(value)
        super().__setitem__(key, value)

    def append(self, obj):
        self.__check_type(obj)
        super().append(obj)
