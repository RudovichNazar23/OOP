class InputValues:
    def __init__(self, render):
        self.render = render

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            return [*(map(self.render, func().split()))]
        return wrapper

class RenderDigit:
    def __call__(self, string):
        try:
            return int(string)
        except:
            return None

input_dg = InputValues(RenderDigit())(input)
res = input_dg()
print(res)
