# Property. Вычисляемые свойства

class Square:
    def __init__(self, side):
        self.__side = side
        self.__area = None

    @property
    def side(self):
        return self.__side

    @side.setter
    def side(self, new_side):
        if isinstance(new_side, (int, float)) and new_side >= 0:
            self.__side = new_side
            self.__area = None

    @property
    def area(self):
        if self.__area is None:
            print("!!!")
            self.__area = self.__side ** 2
        return self.__area

a = Square(5)
print(a.area)
print(a.area)

a.side = 7
print(a.area)


