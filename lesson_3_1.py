# Магические методы __sts__ и __repr__

class Leon:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"The object Leon - {self.name}"

    def __str__(self):
        return f"Leon - {self.name}"

a = Leon("Misha")
print(a)
