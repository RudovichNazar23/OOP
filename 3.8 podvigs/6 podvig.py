
class StackObj:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.amount_obj = 0

    def push(self, obj):
        if self.top is None:
            self.top = obj
            self.amount_obj += 1
        else:
            current = self.top
            while current.next is not None:
                current = current.next
            current.next = obj
            self.amount_obj += 1

    def pop(self):
        if self.top is None:
            return None
        elif self.top.next is None:
            obj = self.top
            self.top = None
            self.amount_obj -= 1
            return obj
        else:
            current = self.top
            while current.next.next:
                current = current.next
            pop = current.next
            current.next = None
            self.amount_obj -= 1
            return pop

    def __check_index(self, ind):
        if not type(ind) == int or not 0 <= ind < self.amount_obj:
            raise IndexError('неверный индекс')

    def __getitem__(self, item):
        self.__check_index(item)
        var = 0
        if self.top is None:
            return None
        else:
            current = self.top
            while var < item:
                current = current.next
                var += 1
            return current

    def __setitem__(self, key, value):
        self.__check_index(key)
        obj = self[key]

        prev = self[key - 1] if key > 0 else None

        value.next = obj.next

        if prev:
            prev.next = value

