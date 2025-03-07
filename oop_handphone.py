# OOP -> Object
# Object (blueprint) -> property, method


class Handphone:
    def __init__(self, brand):
        self.brand = brand
        self.is_active = False

    def turn_on(self):
        self.is_active = True
        print(f"Handpone {self.brand} is turned on!")

    def turn_off(self):
        self.is_active = False
        print(f"Handpone {self.brand} is turned off!")


# create 1st object
oppo = Handphone("Oppo")

print("Before turn on:", oppo.is_active)
oppo.turn_on()
print("After turn on:", oppo.is_active)

print("*" * 45)


# create 2nd object
samsung = Handphone("Samsung")

print("Before turn on:", samsung.is_active)
samsung.turn_on()
print("After turn on:", samsung.is_active)

print("*" * 45)
# create 3rd object
xiaomi = Handphone("Xiaomi")

print("Before turn on:", xiaomi.is_active)
xiaomi.turn_on()
print("After turn on:", xiaomi.is_active)
