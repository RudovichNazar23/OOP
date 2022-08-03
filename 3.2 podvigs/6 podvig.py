class RenderList:
    def __init__(self, type_list):
        self.type_list = type_list

    def __call__(self, lst, **kwargs):
        for i in range(len(lst)):
            if self.type_list == "ol":
                return "<ol>" + "\n<li>" + "</li>\n<li>".join(lst) + "</li>\n" + "</ol>"
        else:
            self.type_list = "ul"
            return "<ul>" + "\n<li>" + "</li>\n<li>".join(lst) + "</li>\n" + "</ul>"

lst = ["1", "2", "3"]

ex = RenderList("ul")
html = ex(lst)
print(html)



