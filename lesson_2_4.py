class Cat:
    __shared_atr = {
        'bread': "pers",
        'age': 10,
        'color': 'black'
    }

    def __init__(self):
        self.__dict__ = Cat.__shared_atr

a = Cat()
print(a.__dict__)

print(Cat().__dict__)

a.bread = "Yellow"
a.say = "Мяу"

print(a.__dict__)
print(Cat().__dict__)
