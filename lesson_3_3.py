# Магические методы
# __add__, __mul__, __sub__ и __truediv__
# отвечают за базовые математическе операции

class BancAccound:
    def __init__(self, name, balance):
        print("New object init")
        self.name = name
        self.balance = balance

    def __repr__(self):
        return f"Клиент {self.name} с балансом {self.balance}"

    def __add__(self, other):
        print("Метод __add__ был вызван")
        if isinstance(other, BancAccound):
            return BancAccound(self.name, self.balance + other.balance)
        if isinstance(other, (int, float)):
            return BancAccound(self.name, self.balance + other)
        raise NotImplemented

    def __radd__(self, other):
        print("__radd__ был вызван")
        return self + other

    def __mul__(self, other):
        print("Метод __mull__ был вызван")
        if isinstance(other, BancAccound):
            return self.balance * other.balance
        if isinstance(other, (int, float)):
            return self.balance * other
        if isinstance(other, str):
            return self.name + other
        raise NotImplemented



