class ImageFileAcceptor:
    def __init__(self, extensions):
        self.extensions = extensions

    def __call__(self, file, *args, **kwargs):
        return file.endswith(self.extensions)

