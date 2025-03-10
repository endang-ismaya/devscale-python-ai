class Animal:
    def __init__(self):
        self.weight = 0

    def set_weight(self, weight):
        self.weight = weight

    def get_weight(self):
        return self.weight

    def walk(self):
        return "The animal is walking"


class Chicken(Animal):
    def __init__(self):
        super().__init__()


chicken = Chicken()

chicken.set_weight(10)
print(chicken.get_weight())
print(chicken.walk())
