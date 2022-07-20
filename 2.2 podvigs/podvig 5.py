class WindowDlg:

    def __init__(self, title: str, width: int, height: int):
        self.__title, self.__width, self.__height = (title, width, height)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width: int):
        if (0 <= width <= 10000) and (type(width)==int):
            if self.__width != width:
                self.__width = width
                self.show()

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height: int):
        if (0 <= height <= 10000) and (type(height)==int):
            if self.__height != height:
                self.__height = height
                self.show()

    def show(self):
        print(f"{self.__title}: {self.__width}, {self.__height}")

