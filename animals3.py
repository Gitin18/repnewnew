



class Zoo:
    def __init__(self):
        self.animals = []
        self.zookeeper = []
        self.veterinarian = []

    def add_zookeeper(self, zookeeper):
        self.zookeeper.append(zookeeper)
        print(f"Zookeeper {zookeeper} added to the staff.")

    def add_veterinarian(self, veterinarian):
        self.veterinarian.append(veterinarian)
        print(f"Veterinarian {veterinarian} added to the stuff")

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"Animal {animal} added to the zoo.")


    def feed_animal(self, zookeeper, animal):
        if zookeeper in self.zookeeper and animal in self.animals:
            print(f"Zookeeper {zookeeper} fed the {animal}.")
        else:
            print("Either the zookeeper or the animal is not available.")

    def heel_animal(self,veterinarian,animal):
        if veterinarian in self.veterinarian and animal in self.animals:
            print(f"Veterinarian {veterinarian} heeled the {animal}.")
        else:
            print("Either the Veterinarian or the animal is not available.")

    def display_zoo(self):
        print(f"Animals in the zoo: {', '.join(self.animals)}")
        print(f"Employees in the zoo: {', '.join(self.zookeeper)}")
        print(f"Employees in the zoo: {', '.join(self.veterinarian)}")

class ZooKeeper:
    def __init__(self, name):
        self.name = name

    def feed_animal(self, zoo, animal):
        if animal in zoo.animals:
            print(f"{self.name} is feeding the {animal}.")
        else:
            print(f"The animal {animal} is not in the zoo.")

# Example Usage
my_zoo = Zoo()
my_zoo.add_zookeeper("John")
my_zoo.add_veterinarian("Sarah")
my_zoo.add_animal("Lion")
my_zoo.add_animal("Tiger")
my_zoo.display_zoo()

my_zoo.feed_animal("John","Tiger")
my_zoo.heel_animal("Sarah","Lion")