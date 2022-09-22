class Car:
    model = "Lada"
    engine = 1.6

    @staticmethod
    def drive():
        print("let's go")

Car.drive()
a = Car()
a.drive()