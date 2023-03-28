from abc import ABC, abstractmethod


class StackInterface(ABC):
    @abstractmethod
    def push_back(self, obj):
        raise NotImplementedError("This method is not redefined")

    @abstractmethod
    def pop_back(self):
        raise NotImplementedError("This method is not redefined")


class StackObj:
    def __init__(self, data):
        self._data = data
        self._next = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, value):
        self._next = value


class Stack(StackInterface):
    def __init__(self):
        self._top = None

    @staticmethod
    def check_obj(obj):
        return obj is None

    def push_back(self, obj):
        if self.check_obj(self._top):
            self._top = obj
        else:
            current = self._top
            while current.next is not None:
                current = current.next
            current.next = obj

    def pop_back(self):
        if self.check_obj(self._top):
            return
        elif self._top.next is None:
            obj = self._top
            self._top = None
            return obj
        else:
            current = self._top
            while current.next.next:
                current = current.next
            del_obj = current.next
            current.next = None

            return del_obj

