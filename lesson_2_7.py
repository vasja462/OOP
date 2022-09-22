# Геттеры, сеттреры и property атрибуты

class BankAccount:
    def __init__(self, name, balance):
        self.__name = name
        self.__balance = balance

    @property
    def my_balance(self):
        return self.__balance

    @my_balance.setter
    def my_balance(self, value):
        if not isinstance(value, (int, float)):
            print("Баланс не является числом")
        self.__balance = value

f = BankAccount("Oleg", 3000)
print(f.my_balance)
f.my_balance += 500
print(f.my_balance)


