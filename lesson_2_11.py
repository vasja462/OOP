# Практика по Property
from string import digits

class User:
    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.__secret = "abracadabra"

    @property
    def secret(self):
        s = input("Введите пароль\n")
        if s == self.password:
            print(self.__secret)
        else:
            print("неверный пароль")
            raise ValueError('Доступ закрыт')

    @property
    def password(self):
        print("getter")
        return self.__password

    @staticmethod
    def is_include_numbers(password):
        for digit in digits:
            if digit in password:
                return True
        return False

    @password.setter
    def password(self, value):
        print("setter")
        if not isinstance(value, str):
            raise TypeError("Пароль должен быть строкой")
        if len(value) < 4 or len(value) > 12:
            raise ValueError("Длина пароля должна быть не менее 4 и не более 12 символов")
        if not User.is_include_numbers(value):
            raise ValueError(" Пароль должен содержать хотя бы 1 цифру")
        self.__password = value


a = User('Ivan', '1231d')
print(a.password)
a.password = "wesd4f"
print(a.password)
a.password = "4fertewrtert"
print(a.password)
a.secret