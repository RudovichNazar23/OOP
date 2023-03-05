class GenericView:
    def __init__(self, methods=('GET',)):
        self.methods = methods

    def get(self, request):
        return ""

    def post(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass


class DetailView(GenericView):
    def render_request(self, request, method):
        if method not in self.methods:
            raise TypeError('данный запрос не может быть выполнен')
        else:
            return getattr(self, method.lower())(request)

    def get(self, request):
        if not type(request) is dict:
            raise TypeError(f"{request} не является словарем")

        elif not request.get("url"):
            raise TypeError(f"{request} не содержит обязательного ключа url")
        else:
            return "url: " + str(request.get("url"))
