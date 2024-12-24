class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def make_sound(self):
        pass

    def eat(self):
        pass
class Bird(Animal):
    def make_sound(self):
        return "Chirik,Chirik"
class Dog(Animal):
    def make_sound(self):
        return "Woof"


class Delfin(Animal):
    def make_sound(self):
        return "PipPip"

def animal_sound(animal):
    print(animal.make_sound())

dog1 = Dog("sharik",14)
bird1 = Bird("Popka",5)
delfin1 = Delfin("Arthur",3)
animal_sound(dog1)
animal_sound(bird1)
animal_sound(delfin1)
