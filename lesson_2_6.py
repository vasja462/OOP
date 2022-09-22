# Геттеры, сеттреры и property атрибуты

class BankAccount:
    def __init__(self, name, balanse):
        self.__name = name
        self.__balance = balanse

    def get_balance(self):
        return self.__balance

    def set_balanse(self, value):
        if not isinstance(value, (int, float)):
            print("Баланс не является числом")
        self.__balance = value

    def delete_balance(self):
        del self.__balance

    many = property(fget=get_balance, fset=set_balanse, fdel=delete_balance)

a = BankAccount("Ivan", 5000)
print(a.many)
a.many = a.many + 500
print(a.many)


