# __eq__ отвечает за ==
# __nq__ отвечает за !=
# __lt__ отвечает за <
# __le__ отвечает за <=
# __gt__ отвечает за >
# __ge__ отвечает за >=

class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @property
    def area(self):
        return self.a * self.b

    def __eq__(self, other):
        print("__eq__ call")
        if isinstance(other, Rectangle):
            return self.a == other.a and self.b == other.b

    def __lt__(self, other):
        print("__lt__ call")
        if isinstance(other, Rectangle):
            return self.area < other.area
        elif isinstance(other, (int, float)):
            return self.area < other

    def __le__(self, other):
        return self == other or self < other








