class LinkedList:
    objects = list()

    def __init__(self):
        if self.objects is None:
            self.head = None
            self.tail = None

    def add_obj(self, obj):
        if isinstance(obj, ObjList):
            self.tail = obj
            self.objects.append(self.tail)

    def remove_obj(self, indx):
        if indx in self.objects:
            self.objects.pop(indx)

    def __len__(self, linked_list):
        return len(linked_list)

    def linked_lst(self, indx):
        if indx in self.objects:
            return self.objects[indx]


class Obj_lstDescriptor:
    def __set_name__(self, owner, name):
        self._name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self._name)


class ObjList:
    prev = Obj_lstDescriptor()
    data = Obj_lstDescriptor()
    next = Obj_lstDescriptor()

    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None

