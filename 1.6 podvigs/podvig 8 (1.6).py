
TYPE_OS = 1  # 1 - Windows; 2 - Linux


class DialogWindows:
    name = "DialogWindows"


class DialogLinux:
    name = "DialogLinux"


class Dialog:
    name = str()

    def __new__(cls, *args, **kwargs):
        cls.args = cls.name
        if TYPE_OS != 1:
            dialog = DialogLinux()
            setattr(dialog, 'name', *args)
            return dialog
        else:
            dialog_2 = DialogWindows()
            setattr(dialog_2, 'name', *args)
            return dialog_2

class_object = Dialog("hello")
print(class_object)
print(class_object.name)


