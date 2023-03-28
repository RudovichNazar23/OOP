
class VideoRating:
    def __init__(self):
        self.__rating = 0

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, value):
        if value in range(0, 6) and type(value) is int:
            self.__rating = value
        else:
            raise ValueError('неверное присваиваемое значение')


class VideoItem:
    def __init__(self, title, descr, path):
        self.title = title
        self.descr = descr
        self.path = path
        self.rating = VideoRating()
