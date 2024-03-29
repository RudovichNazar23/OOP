class Video:
    def create(self, name):
        self.name = name
        return name

    def play(self):
        print("воспроизведение видео " + str(self.name))


class YouTube:
    videos = list()

    @classmethod
    def add_video(cls, video):
        cls.videos.append(video)

    @classmethod
    def play(cls, video_indx):
        return cls.videos[video_indx].play()

v1 = Video()
v1.create("Python")
v2 = Video()
v2.create("Python ООП")
YouTube.add_video(v1)
YouTube.play(0)
YouTube.add_video(v2)
YouTube.play(1)
