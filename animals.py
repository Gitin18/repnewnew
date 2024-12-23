class Animal():
    def make_sound(self):
        pass

    def eat(self):
        pass
class Bird(Animal):
    def make_sound(self):
        return "Lala"
class Dog(Animal):
    def make_sound(self):
        return "Woof"


class Delfin(Animal):
    def make_sound(self):
        return "PipPip"
def animal_sound(animal):
    print(animal.make_sound())
dog1 = Dog()
bird1 = Bird()
delfin1= Delfin()
animal_sound(dog1)
animal_sound(bird1)
animal_sound(delfin1)
