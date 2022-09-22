# classmethod и staticmethod

class Example:
    def hello():
        print("hello")
        print("Можем вызвать от класса, но не можем вызвать от экземпляра")

    def instance_hello(self):
        print(f'instance_hello {self}')
        print("Можем вызвать от экземпляра, но не можем вызвать от класса")

    @staticmethod
    def static_hello():
        print(f'static_hello')
        print("Можем вызвать от класса и от экземряра")

    @classmethod
    def class_hello(cls):
        print(f"class_hello {cls}")
        print("""Можем вызвать от класса и от экземряра. Первым параметром принимает 
класс (cls) В cls - при вызове от экз. класса попадет экз.""")

a = Example()
Example.hello()
a.instance_hello()

Example.static_hello()
a.static_hello()

Example.class_hello()
a.class_hello()