class Cat:
    def __init__(self, name, age, bread, color):
        print(f'объект: {self}\nимя: {name}\nвозраст: {age}\nпорода: {bread}\nцвет: {color}')
        self.name = name
        self.age = age
        self.bread = bread
        self.color = color

jerry = Cat(name="Jerry", age=1, bread="pers", color="yellow")
