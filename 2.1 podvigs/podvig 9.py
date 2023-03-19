class ObjList:
    def __init__(self, data: str):
        self.__data = data
        self.__next = None
        self.__prev = None

    def set_next(self, obj=None):
        self.__next = obj

    def set_prev(self, obj):
        self.__prev = obj

    def get_next(self):
        return self.__next

    def get_prev(self):
        return self.__prev

    def set_data(self, value):
        self.__data = value

    def get_data(self):
        return self.__data


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_obj(self, obj):
        if self.tail:
            self.tail.set_next(obj)
        obj.set_prev(self.tail)
        self.tail = obj
        if self.head is None:
            self.head = obj

    def remove_obj(self):
        if self.tail is None:
            return

        prev = self.tail.get_prev()
        if prev:
            prev.set_next(None)

        self.tail = prev
        if self.tail is None:
            self.head = None

    def get_data(self):
        lst = []
        current = self.head
        while current:
            lst.append(current.get_data())
            current = current.get_next()
        return lst

