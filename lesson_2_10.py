# Пространство имен класса

class DepartmentID:
    P1 = 1
    P2 = 2
    P3 = 3

    def info(self):
        print(self.P1, self.P2, self.P3)

    def info2(self):
        print(DepartmentID.P1, DepartmentID.P2, DepartmentID.P3)

    @property
    def info3(self):
        print(self.P1, self.P2, self.P3)

    @classmethod
    def info4(cls):
        print(cls.P1, cls.P2, cls.P3)

    @staticmethod
    def info5():
        print(DepartmentID.P1, DepartmentID.P2, DepartmentID.P3)

    def plus_1(self):
        DepartmentID.P1 += 1

r1 = DepartmentID()
r1.info()
r1.info2()
r1.info3
r1.info4()
r1.info5()
print(DepartmentID.P1)
r1.plus_1()
print(DepartmentID.P1)

print()
r2 = DepartmentID()
r2.P1
r2.plus_1()
print(r2.P1)
print(DepartmentID.P1)