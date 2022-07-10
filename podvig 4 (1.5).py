'''import random

class Line:
    def __init__(self, a=0, b=0, c=0, d=0):
        self.sp = (a, b)
        self.ep = (c, d)


class Rect:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


class Ellipse:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


elements = []

for obj in range(217):
    a = random.randint(0,9)
    b = random.randint(0, 9)
    c = random.randint(0, 9)
    d = random.randint(0, 9)
    elements.append(random.choice([Line(0, 0, 0, 0), Rect(a, b, c, d), Ellipse(a, b, c, d)]))
print(elements)
'''


def check(a, b, c):
    if a == float or a <= 0:
        return 1
    elif b == float or b <= 0:
        return 1
    elif c == float or c <= 0:
        return 1

    elif a + b <= c:
        return 2

    elif b + c <= a:
        return 2

    elif a + c <= b:
        return 2

    else:
        return True


func = check()
print(func)

"""
Возвращаем 1, если переданные значения нецелочисленные, а также если хотя бы одно число меньше или равно нулю.

Возвращаем 2, если такой треугольник не может быть образован. 

Возвращаем 3,  если такой треугольник может быть образован. 


"""