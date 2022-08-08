class ObjList:
    def __init__(self, data):
        self.__data = data
        self.__next = None
        self.__prev = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, obj):
        if self.check(obj):
            self.__next = obj

    @property
    def prev(self):
        return self.__prev

    @prev.setter
    def prev(self, obj):
        if self.check(obj):
            self.__prev = obj

    @staticmethod
    def check(x):
        return isinstance(x, ObjList) or x is None


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_obj(self, obj):
        if self.head is None:
            self.head = obj
            self.tail = self.head
        else:
            self.tail.next = obj
            obj.prev = self.tail
            self.tail = obj

    def remove_obj(self, indx):

        if self.head is None:
            return

        if 0 <= indx < len(self):
            j = self.head
            for i in range(indx):
                j = j.next
            if j == self.head:
                if j.next is not None:
                    self.head = j.next
                else:
                    self.head = None
                    self.tail = None
                self.head = j.next
            if j.prev is not None:
                j.prev.next = j.next
            if j.next is not None:
                j.next.prev = j.prev
            if self.tail == j:
                self.tail = j.prev



    def __len__(self):
        if self.head is None:
            return 0
        else:
            counter = 1
            i = self.head
            while i.next:
                i = i.next
                counter += 1
            return counter

    def __call__(self, *args, **kwarg):
        if 0 <= args[0] < len(self):
            j = self.head
            for i in range(args[0]):
                j = j.next
            return j.data
        else:
            return

    @staticmethod
    def check_class(x):
        return isinstance(x, ObjList)
