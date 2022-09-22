class Cat:
    bread = "seam"

    def show_bread(instanse):
        print(f"my bread is {instanse.bread}")

    def show_name(instanse):
        if hasattr(instanse, 'name'):
            print(f"my name is {instanse.name}")
        else:
            print('у кота нет имени')

    def set_name(self, value):
        self.name = value

a = Cat()
a.bread = "pers"
a.show_bread()
a.show_name()

mary = Cat()
mary.name = "Mary"
mary.show_name()

tom = Cat()
tom.set_name("Tom")
print(tom.name)
tom.show_name()
