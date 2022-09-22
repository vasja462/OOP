# class Robot:
#     def say_hello(self):
#         print("Hello, human! My name is C-3PO")
#
#     def say_bye(self):
#         print("See u later alligator")
#
#
# c3po = Robot()
# r2d2 = Robot()
#
# c3po.say_hello()
# c3po.say_bye()
#
# r2d2.say_hello()
# r2d2.say_bye()
#
# class Robot:
#     def say_hello(self):
#         if hasattr(self, 'name'):
#             print(f"Hello, human! My name is {self.name}")
#         else:
#             print("У робота нет имени")
#
#     def say_bye(self):
#         print("See u later alligator")
#
#     def set_name(self, name):
#         self.name = name
#
# c3po = Robot()
# c3po.say_hello() # печатает У робота нет имени
# c3po.set_name('R2D2')
# c3po.say_hello() # печатает Hello, human! My name is R2D2
# c3po.say_bye() # печатает See u later alligator
#
# r = Robot()
# r.set_name('Chappy')
# r.say_hello()# печатает Hello, human! My name is Chappy

# class Counter:
#     def start_from(self, value=0):
#         self.value = value
#
#     def increment(self):
#         self.value += 1
#
#     def display(self):
#         print(f"Текущее значение счетчика = {self.value}")
#
#     def reset(self):
#         self.value = 0

# c1 = Counter()
# c1.start_from()
# c1.increment()
# c1.display() # печатает "Текущее значение счетчика = 1"
# c1.increment()
# c1.display() # печатает "Текущее значение счетчика = 2"
# c1.reset()
# c1.display() # печатает "Текущее значение счетчика = 0"
#
# c2 = Counter()
# c2.start_from(3)
# c2.display() # печатает "Текущее значение счетчика = 3"
# c2.increment()
# c2.display() # печатает "Текущее значение счетчика = 4"

# class Constructor:
#     def add_atribute(self, name, value):
#         setattr(self, name, value)
#
#     def display(self):
#         print(self.__dict__)
#
# obj1 = Constructor()
# obj1.display() # печатает {}
# obj1.add_atribute('color', 'red')
# obj1.add_atribute('width', 20)
# obj1.display() # печатает {'color': 'red', 'width': 20}
#
# obj2 = Constructor()
# obj2.display() # печатает {}
# obj2.add_atribute('height', 100)
# obj2.display() # печатает {'height': 100}

from math import sqrt

from math import sqrt

# class Point:
#     def set_coordinates(self, x, y):
#         self.x = x
#         self.y = y
#
#     def get_distance(self, object):
#         if isinstance(object, Point):
#             return f'sqrt((object.x - self.x) ** 2 + (object.y - self.y) ** 2)'
#
#         else:
#             return "Передана не точка"

# p1 = Point()
# p2 = Point()
# p1.set_coordinates(1, 2)
# p2.set_coordinates(4, 6)
# d = p1.get_distance(p2) # вернёт 5.0
# p1.get_distance(10) # Распечатает "Передана не точка"
#
# p3 = Point()
# p4 = Point()
# p3.set_coordinates(0, 0)
# p4.set_coordinates(3, 4)
# d = p3.get_distance(p4)

# class Vehicle:
#     def __init__(self, max_speed, mileage):
#         self.max_speed = max_speed
#         self.mileage = mileage
#
# modelX = Vehicle(240, 18)
# print(modelX.max_speed, modelX.mileage)# 240 18


# class Laptop:
#     def __init__(self, brand, model, price):
#         self.brand = brand
#         self.model = model
#         self.price = price
#         self.laptop_name = f"{self.brand} {self.model}"
#
# laptop1 = Laptop('macbook', 'mb-2022', 100000)
# laptop2 = Laptop('lenovo', 'ln-22', 25000)
#
# print(laptop1.laptop_name)
# print(laptop2.laptop_name)

# class SoccerPlayer:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#         self.goals = 0
#         self.assists = 0
#
#     def score(self, goals=1):
#         self.goals += goals
#
#     def make_assist(self, assists=1):
#         self.assists += assists
#
#     def statistics(self):
#         print(f"{self.surname} {self.name} - голы: {self.goals}, передачи: {self.assists}")

# leo = SoccerPlayer('Leo', 'Messi')
# leo.score(700)
# leo.make_assist(500)
# leo.statistics() # выводит "Messi Leo - голы: 700, передачи: 500"
# kokorin = SoccerPlayer('Alex', 'Kokorin')
# kokorin.score()
# kokorin.statistics() # выводит "Kokorin Alex - голы: 1, передачи: 0"

# class Zebra:
#     def __init__(self):
#         self.poloska = "Полоска белая"
#
#     def which_stripe(self):
#         print(self.poloska)
#         if self.poloska == "Полоска белая":
#             self.poloska = "Полоска черная"
#         else:
#             self.poloska = "Полоска белая"

# z1 = Zebra()
# z1.which_stripe() # печатает "Полоска белая"
# z1.which_stripe() # печатает "Полоска черная"
# z1.which_stripe() # печатает "Полоска белая"
#
# z2 = Zebra()
# z2.which_stripe() # печатает "Полоска белая"

# class Person:
#     def __init__(self, first_name, last_name, age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#
#     def full_name(self):
#         return f"{self.last_name} {self.first_name}"
#
#     def is_adult(self):
#         return self.age >= 18
#
# p1 = Person('Jimi', 'Hendrix', 5)
# print(p1.full_name())  # выводит "Hendrix Jimi"
# print(p1.is_adult()) # выводит "True"
#
# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def description(self):
#         return f'{self.name} is {self.age} years old'
#
#     def speak(self, sound):
#         self.sound = sound
#         return f'{self.name} says {self.sound}'
#
# jack = Dog("Jack", 4)
#
# print(jack.description()) # распечатает 'Jack is 4 years old'
# print(jack.speak("Woof Woof")) # распечатает 'Jack says Woof Woof'
# print(jack.speak("Bow Wow")) # распечатает 'Jack says Bow Wow'

# class Stack:
#     def __init__(self):
#         self.values = []
#
#     def push(self, item):
#         self.values.append(item)
#
#     def pop(self):
#         if len(self.values) > 0:
#             return self.values.pop()
#         print("Empty Stack")
#
#     def peek(self):
#         if len(self.values) > 0:
#             return self.values[-1]
#         print("Empty Stack")
#
#     def is_empty(self):
#         return len(self.values) == 0
#
#     def size(self):
#         return len(self.values)
#
# s = Stack()
# s.peek()  # распечатает 'Empty Stack'
# print(s.is_empty())  # распечатает True
# s.push('cat')  # кладем элемент 'cat' на вершину стека
# s.push('dog')  # кладем элемент 'dog' на вершину стека
# print(s.peek())  # распечатает 'dog'
# s.push(True)  # кладем элемент True на вершину стека
# print(s.size())  # распечатает 3
# print(s.is_empty())  # распечатает False
# s.push(777)  # кладем элемент 777 на вершину стека
# print(s.pop())  # удаляем элемент 777 с вершины стека и печатаем его
# print(s.pop())  # удаляем элемент True с вершины стека и печатаем его
# print(s.size())  # распечатает 2

# class Worker:
#     def __init__(self, name, salary, gender, passport):
#         self.name = name
#         self.salery = salary
#         self.gender = gender
#         self.passport = passport
#
#     def get_info(self):
#         print(f"Worker {self.name}; passport-{self.passport}")
#
# persons = [
#     ('Allison Hill', 334053, 'M', '1635644202'),
#     ('Megan Mcclain', 191161, 'F', '2101101595'),
#     ('Brandon Hall', 731262, 'M', '6054749119'),
#     ('Michelle Miles', 539898, 'M', '1355368461'),
#     ('Donald Booth', 895667, 'M', '7736670978'),
#     ('Gina Moore', 900581, 'F', '7018476624'),
#     ('James Howard', 460663, 'F', '5461900982'),
#     ('Monica Herrera', 496922, 'M', '2955495768'),
#     ('Sandra Montgomery', 479201, 'M', '5111859731'),
#     ('Amber Perez', 403445, 'M', '0602870126')
# ]
#
# worker_objects = []
#
# for person in persons:
#     worker_objects.append(Worker(*person))
#     worker_objects[-1].get_info()

# class CustomLabel:
#     def __init__(self, text, **qwargs):
#         self.text = text
#         for i in qwargs:
#             self.__dict__[i] = qwargs[i]
#
#
#     def config(self, **qwargs):
#         for i in qwargs:
#             self.__dict__[i] = qwargs[i]
#
# label = CustomLabel(text="Hello", bd=20, bg='#ffaaaa')
#
# print(label.__dict__) # {'text': 'Hello', 'bd': 20, 'bg': '#ffaaaa'}
#
# label.config(color='red', bd=100)
#
# print(label.__dict__) # {'text': 'Hello', 'bd': 100, 'bg': '#ffaaaa', 'color': 'red'}
#
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def display_person_info(self):
#         print(f"Person: {self.name}, {self.age}")
#
#
# class Company:
#     def __init__(self, company_name, location):
#         self.company_name = company_name
#         self.location = location
#
#     def display_company_info(self):
#         print(f"Company: {self.company_name}, {self.location}")
#
#
# class Employee:
#     def __init__(self, name, age, company_name, location):
#         self.personal_data = Person(name, age)
#         self.work = Company(company_name, location)
#
# emp = Employee('Jessica', 28, 'Google', 'Atlanta')
# print(emp.personal_data.name)
# print(emp.personal_data.age)
# emp.personal_data.display_person_info()
# print(emp.work.company_name)
# print(emp.work.location)
# emp.work.display_company_info()

# class Student:
#     def __init__(self, name, age, branch):
#         self.__name = name
#         self.__age = age
#         self.__branch = branch
#
#     def __display_details(self):
#         print(f"Имя: {self.__name}")
#         print(f"Возраст: {self.__age}")
#         print(f"Направление: {self.__branch}")
#
#     def access_private_method(self):
#         self.__display_details()
#
# obj = Student("Adam Smith", 25, "Information Technology")
# obj.access_private_method()
#
# class PizzaMaker:
#     def __make_pepperoni(self):
#         pass
#
#     def _make_barbecue(self):
#         pass
#
# maker = PizzaMaker()
#
# print(dir(maker))
#
# print(maker._make_barbecue)
# print(maker._PizzaMaker__make_pepperoni)
#
# class UserMail:
#     def __init__(self, login, email):
#         self.login = login
#         self.__email = email
#
#     def get_email(self):
#         return self.__email
#
#     def set_email(self, value:str):
#         if isinstance(value, str) and value.count("@") == 1 and "." in value[value.index("@"):]:
#             self.__email = value
#         else:
#             print(f'ErrorMail:{value}')
#
#     email = property(fget=get_email, fset=set_email)
#
# k = UserMail('belosnezhka', 'prince@wait.you')
# print(k.email)  # prince@wait.you
# k.email = [1, 2, 3] # ErrorMail:[1, 2, 3]
# k.email = 'prince@still@.wait'  # ErrorMail:prince@still@.wait
# k.email = 'prince@still.wait'
# print(k.email)  # prince@still.wait

# class Notebook:
#     def __init__(self, notes:list):
#         self._notes = notes
#
#     @property
#     def notes_list(self):
#         for i, note in enumerate(self._notes):
#             print(f"{i+1}.{note}")
#
# note = Notebook(['Buy Potato', 'Buy Carrot', 'Wash car'])
# note.notes_list

# class Money:
#     def __init__(self, dollars, cents):
#         self.total_cents = dollars * 100 + cents
#
#     @property
#     def dollars(self):
#         return self.total_cents // 100
#
#     @dollars.setter
#     def dollars(self, new_dollars):
#         if isinstance(new_dollars, int) and new_dollars >= 0:
#             self.total_cents = new_dollars * 100 + self.total_cents % 100
#         else:
#             print("Error dollars")
#
#     @property
#     def cents(self):
#         return self.total_cents % 100
#
#     @cents.setter
#     def cents(self, new_cents):
#         if isinstance(new_cents, int) and 100 > new_cents >= 0:
#             self.total_cents = self.total_cents // 100 * 100 + new_cents
#         else:
#             print("Error cents")
#
#     def __str__(self):
#         return f"Ваше состояние составляет {self.dollars} долларов {self.cents} центов"

# Bill = Money(101, 99)
# print(Bill)  # Ваше состояние составляет 101 долларов 99 центов
# print(Bill.dollars, Bill.cents)  # 101 99
# print(Bill.total_cents) # 10199
# Bill.dollars = 666
# print(Bill)  # Ваше состояние составляет 666 долларов 99 центов
# Bill.cents = 12
# print(Bill)  # Ваше состояние составляет 666 долларов 12 центов
#
# class Rectangle:
#     def __init__(self, h, t):
#         self.h = h
#         self.t = t
#
#     @property
#     def area(self):
#         return self.h * self.t
#
# r1 = Rectangle(3, 5)
# r2 = Rectangle(6, 1)
#
# print(r1.area) # 15
# print(r2.area) # 6

# class Date:
#     def __init__(self, d, m, y):
#         if d >= 10:
#             self.d = str(d)
#         else:
#             self.d = f'0{d}'
#
#         if m >= 10:
#             self.m = str(m)
#         else:
#             self.m = f'0{m}'
#
#         if y >= 1000:
#             self.y = str(y)
#         elif y >= 100:
#             self.y = f'0{y}'
#         elif y >= 10:
#             self.y = f'00{y}'
#         else:
#             self.y = f'000{y}'
#
#     @property
#     def date(self):
#         return f"{self.d}/{self.m}/{self.y}"
#
#     @property
#     def usa_date(self):
#         return f"{self.m}-{self.d}-{self.y}"
#
# d1 = Date(5, 10, 2001)
# d2 = Date(15, 3, 999)
#
# print(d1.date) # 05/10/2001
# print(d1.usa_date) # 10-05-2001
# print(d2.date) # 15/03/0999
# print(d2.usa_date) # 03-15-0999
#
# class Robot:
#     population = 0
#
#     def __init__(self, name):
#         self.name = name
#         Robot.population += 1
#         print(f"Робот {self.name} был создан")
#
#     def destroy(self):
#         Robot.population -= 1
#         print(f"Робот {self.name} был уничтожен")
#
#     def say_hello(self):
#         print(f"Робот {self.name} приветствует тебя, особь человеческого рода")
#
#     @classmethod
#     def how_many(cls):
#         print(f"{cls.population}, вот сколько нас еще осталось")
#
# r2 = Robot("R2-D2") # печатает "Робот R2-D2 был создан"
# r2.say_hello() # печатает "Робот R2-D2 приветствует тебя, особь человеческого рода"
# Robot.how_many() # печатает "1, вот сколько нас еще осталось"
# r2.destroy() # печатает "Робот R2-D2 был уничтожен"
# Robot.how_many()
#
# class User:
#     def __init__(self, name, role):
#         self.name = name
#         self.role = role
#
#
# class Access:
#     __access_list = ['admin', 'developer']
#
#     @staticmethod
#     def __check_access(role):
#         return role in Access.__access_list
#
#     @staticmethod
#     def get_access(d):
#         if isinstance(d, User):
#             if Access.__check_access(d.role):
#                 print(f"User {d.name}: success")
#             else:
#                 print("AccessDenied")
#         else:
#             print(f"AccessTypeError")
#
# user1 = User('batya99', 'admin')
# Access.get_access(user1) # печатает "User batya99: success"
#
# zaya = User('milaya_zaya999', 'user')
# Access.get_access(zaya) # печатает AccessDenied
#
# Access.get_access(5) # печатает AccessTypeError
#
# from string import digits, ascii_lowercase, ascii_letters
#
# class Registration:
#     def __init__(self, login, value):
#         self.login = login
#         self.password = value
#
#     @property
#     def login(self):
#         return self.__login
#
#     @login.setter
#     def login(self, value:str):
#         if value.count("@") != 1:
#             raise ValueError("Логин должен содержать один символ '@'")
#         if "." not in value[value.index("@"):]:
#             raise ValueError("Логин должен содержать символ '.'")
#
#         self.__login = value
#
#     @property
#     def password(self):
#         return self.__password
#
#     @staticmethod
#     def is_include_digit(value):
#         for digit in digits:
#             if digit in value:
#                 return True
#         return False
#
#     @staticmethod
#     def is_include_all_register(value):
#
#         flag = False
#         for lowercase in ascii_lowercase:
#             if lowercase in value:
#                 flag = True
#         if flag:
#             for lowercase in ascii_lowercase:
#                 if lowercase.upper() in value:
#                     return True
#             return False
#
#     @staticmethod
#     def is_include_only_latin(value):
#         for symbol in value:
#             if symbol not in ascii_letters + digits:
#                 return False
#             return True
#
#     @staticmethod
#     def check_password_dictionary(value):
#         file_passwords = open("easy_passwords.txt", "r", encoding="UTF-8")
#         list_file_passwords = file_passwords.read()
#         if value in list_file_passwords:
#             return True
#         return False
#
#     @password.setter
#     def password(self, value):
#         if not isinstance(value, str):
#             raise TypeError("Пароль должен быть строкой")
#         if len(value) <= 4 or len(value) >= 12:
#             raise ValueError('Пароль должен быть длиннее 4 и меньше 12 символов')
#         if not Registration.is_include_digit(value):
#             raise ValueError('Пароль должен содержать хотя бы одну цифру')
#         if not Registration.is_include_all_register(value):
#             raise ValueError('Пароль должен содержать хотя бы один символ верхнего и нижнего регистра')
#         if not Registration.is_include_only_latin(value):
#             raise ValueError('Пароль должен содержать только латинский алфавит')
#         if Registration.check_password_dictionary(value):
#             raise ValueError('Ваш пароль содержится в списке самых легких')
#         self.__password = value
#
#
# r1 = Registration('qwerty@rambler.ru', 'QwrRt124') # здесь хороший логин
# print(r1.login, r1.password)  # qwerty@rambler.ru QwrRt124
#
# теперь пытаемся запись плохие пароли
# r1.password = '123456'  # ValueError('Пароль должен содержать хотя бы один символ верхнего и нижнего регистра')
# r1.password = 'LoW'  # raise ValueError('Пароль должен быть длиннее 4 и меньше 12 символов')
# r1.password = 43  # raise TypeError("Пароль должен быть строкой")
#
# # теперь пытаемся запись плохой логин
# r1.login = '123456'  # ValueError("Логин должен содержать один символ '@'")
#
# r2 = Registration('qwerty.ru')  # ValueError("Логин должен содержать один символ '@'")
# r3 = Registration('qwerty@ru')  # ValueError("Логин должен содержать символ '.'")

# class File:
#     def __init__(self, name):
#         self.name = name
#         self.in_trash = False
#         self.is_deleted = False
#
#     def restore_from_trash(self):
#         print(f"Файл {self.name} восстановлен из корзины")
#         self.in_trash = False
#
#     def remove(self):
#         print(f"Файл {self.name} был удален")
#         self.is_deleted = True
#
#     def read(self):
#         if self.is_deleted:
#             print(f"ErrorReadFileDeleted({self.name})")
#         elif self.in_trash:
#             print(f"ErrorReadFileTrashed({self.name})")
#         else:
#             print(f"Прочитали все содержимое файла {self.name}")
#
#     def write(self, content):
#         if self.is_deleted:
#             print(f"ErrorWriteFileDeleted({self.name})")
#
#         elif self.in_trash:
#             print(f"ErrorWriteFileTrashed({self.name})")
#
#         else:
#             self.content = content
#             print(f"Записали значение {content} в файл {self.name}")
#
# class Trash:
#     content = []
#
#     @staticmethod
#     def add(file):
#         if not isinstance(file, File):
#             print("В корзину добавлять можно только файл")
#         else:
#             Trash.content.append(file)
#             file.in_trash = True
#
#     @staticmethod
#     def clear():
#         print("Очищаем корзину")
#         for file in Trash.content:
#             file.remove()
#         Trash.content.clear()
#         print("Корзина пуста")
#
#     @staticmethod
#     def restore():
#         print("Восстанавливаем файлы из корзины")
#         for file in Trash.content:
#             file.restore_from_trash()
#         Trash.content.clear()
#         print("Корзина пуста")

# from collections import defaultdict
#
# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
#     def __lt__(self, other):
#         return self.name < other.name
#
# class User:
#     def __init__(self, login, balance=0):
#         self.login = login
#         self.balance = balance
#
#     def __str__(self):
#         return f'Пользователь {self.login}, баланс - {self.balance}'
#
#     @property
#     def balance(self):
#         return self.__balance
#
#     @balance.setter
#     def balance(self, new_balance):
#         self.__balance = new_balance
#
#     def deposit(self, sum):
#         self.balance += sum
#
#     def payment(self, sum):
#         if sum > self.__balance:
#             print("Не хватает средств на балансе. Пополните счет")
#             return False
#         self.__balance -= sum
#         return True
#
#
# class Cart:
#     def __init__(self, user):
#         self.user = user
#         self.goods = defaultdict()
#         self.__total = 0
#
#     def add(self, product, amount=1):
#         self.goods[product] = self.goods.get(product, 0) + amount
#         self.__total += product.price * amount
#
#     def remove(self, product, amount=1):
#         if self.goods[product] <= amount:
#             amount = self.goods[product]
#             del self.goods[product]
#         else:
#             self.goods[product] = self.goods[product] - amount
#         self.__total -= product.price * amount
#
#     @property
#     def total(self):
#         return self.__total
#
#     def order(self):
#         if self.user.payment(self.__total):
#             print("Заказ оплачен")
#         else:
#             print("Проблема с оплатой")
#
#     def print_check(self):
#
#         print("---Your check---")
#         result = []
#         for good in self.goods:
#             result.append(f"{good.name} {good.price} {self.goods[good]} {good.price*self.goods[good]}")
#         result.sort()
#         for i in result:
#             print(i)
#
        # print(f'---Total: {self.total}---')

# class Person:
#     def __init__(self, name, surname, gender="male"):
#         if gender not in ["male", "female"]:
#             print("Не знаю, что вы имели ввиду? Пусть это будет мальчик!")
#             gender = "male"
#         self.gender = gender
#         self.name = name
#         self.surname = surname
#
#     def __str__(self):
#         if self.gender == "male":
#             return f"Гражданин {self.surname} {self.name}"
#         return f"Гражданка {self.surname} {self.name}"

# class Vector:
#     def __init__(self, *args):
#         filter_func = lambda x: not isinstance(x, bool) and isinstance(x, int)
#         self.values = sorted(list(filter(filter_func, args)))
#
#     def __str__(self):
#         if len(self.values) > 0:
#             return f"Вектор{tuple(self.values)}"
#         else:
#             return "Пустой вектор"
#
#     def __repr__(self):
#         if len(self.values) > 0:
#             return f"Вектор{tuple(self.values)}"
#         else:
#             return "Пустой вектор"
#
#     def __add__(self, other):
#         if isinstance(other, int):
#             return Vector(*[num + other for num in self.values])
#         if isinstance(other, Vector) and len(self.values) == len(other.values):
#             return Vector(*[i + j for i, j in zip(self.values, other.values)])
#         if isinstance(other, Vector):
#             return print("Сложение векторов разной длины недопустимо")
#         return print(f"Вектор нельзя сложить с {other}")
#
#     def __mul__(self, other):
#         if isinstance(other, int):
#             return Vector(*[num * other for num in self.values])
#         if isinstance(other, Vector) and len(self.values) == len(other.values):
#             return Vector(*[i * j for i, j in zip(self.values, other.values)])
#         if isinstance(other, Vector):
#             return print("Умножение векторов разной длины недопустимо")
#         return print(f"Вектор нельзя умножать с {other}")
#
#
# v1 = Vector(1,2,3)
# print(v1) # печатает "Вектор(1, 2, 3)"
#
# v2 = Vector(3,4,5)
# print(v2) # печатает "Вектор(3, 4, 5)"
# v3 = v1 + v2
# print(v3) # печатает "Вектор(4, 6, 8)"
# v4 = v3 + 5
# print(v4) # печатает "Вектор(9, 11, 13)"
# v5 = v1 * 2
# print(v5) # печатает "Вектор(2, 4, 6)"
# v5 + 'hi' # печатает "Вектор нельзя сложить с hi"

class ChessPlayer:
    def __init__(self, name, surname, rating):
        self.name = name
        self.surname = surname
        self.rating = rating

    def __eq__(self, other):
        if isinstance(other, int):
            return self.rating == other
        elif isinstance(other, ChessPlayer):
            return self.rating == other.rating
        else:
            return "Невозможно выполнить сравнение"

    def __gt__(self, other):
        if isinstance(other, int):
            return self.rating > other
        elif isinstance(other, ChessPlayer):
            return self.rating > other.rating
        else:
            return "Невозможно выполнить сравнение"

    def __lt__(self, other):
        if isinstance(other, (int, ChessPlayer)):
            return not self.__gt__(other) and not self.__eq__(other)
        return 'Невозможно выполнить сравнение'


magnus = ChessPlayer('Carlsen', 'Magnus', 2847)
ian = ChessPlayer('Ian', 'Nepomniachtchi', 2789)
# print(magnus == 4000) # False
# print(ian == 2789) # True
# print(magnus == ian) # False
# print(magnus > ian) # True
# print(magnus < ian) # False
# print(magnus > [22343])
print(magnus < [1, 2])