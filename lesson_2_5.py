class BankAccount:
    def __init__(self, name, balasce, passport):
        self.name = name # Публичный метод
        self.__balance = balasce # Приватрый метод
        self._passport = passport # Защищенный метод

    def print_name(self):
        print(f"Имя клиента:{self._name}")

    def print_balance(self):
        print(f"Баланс :{self.__balance}")

    def print_passport(self):
        print(f"Passport :{self.__balance}")

    def __print_balance1(self): # Приватрый метод
        print(f"Баланс :{self.__balance}")

    def _print_passport1(self): # Защищенный метод
        print(f"Passport :{self.__balance}")

accound1 = BankAccount("Иван", 10000, 4254345342)
print(accound1.name) #  распечатает имя
print(accound1._passport) #  распечатает паспорт
# print(accound1.__balance) #   выведет ошибку
accound1.print_passport() #  распечатает паспорт
accound1.print_balance() #  распечатает баланс (без ошибки)
accound1._print_passport1() #  #  распечатает паспорт
# accound1.__print_balance1() #  будет ошибка

print(dir(accound1)) #
accound1._BankAccount__print_balance1 # будет распечатан баланс

