class Mammal:
    def __init__(self, species, size, weight, habitat):
        self.species = species
        self.size = size
        self.weight = weight
        self.habitat = habitat
        self.isPredator = False


    def eat(self):
        print(f"{self.species} is eating")

    def sleep(self):
        print(f"{self.species} is sleeping")




class Dog(Mammal):

    def __init__(self, breed, preferredFood, favouriteToy):
        self.breed = breed
        self.preferredFood = preferredFood
        self.favouriteToy = favouriteToy


    def bark(self):
        print(f"{self.species}: BARK! BARK!")


class Cat(Mammal):
    def __init__(self, breed, preferredFood, climbingSkill, size, weight, habitat):
        self.breed = breed
        self.preferredFood = preferredFood
        self.climbingSkill = climbingSkill
        self.huntedMouse = None
        super().__init__(species="Cat", size = size, weight = weight, habitat = habitat)

    def hunt_mouse(self, mouse):
        self.huntedMouse = mouse
        print(f"{mouse.name} is being hunted!")
    
    def __str__(self):
        return self.species


class Mouse(Mammal):

    def __init__(self, length, name, size, weight, habitat): 
        self.length = length
        self.name = name
        super().__init__(species="Mouse", size = size, weight = weight, habitat = habitat)
    
    def escape_from_cat(self):
        print(f"{self.name} is running as fast as possible")

    def __str__(self):
        return self.species

louie = Mouse(12, "louie", "small", 1, "City")

max = Cat("Ragdoll", "Fish", "Poor", "Medium", 5, "City")

max.hunt_mouse(louie)


class Habitat:
    def __init__(self, type, temperature, biome):
        self.type = type
        self.temperature = temperature
        self.biome = biome
        self.inhabitants = []

    def add_inhabitant(self, new_inhabitant):
        self.inhabitants.append(new_inhabitant)

    def rain(self):
        self.temperature -= 3
        print("It started raining")
    
    def print_inhabitants(self):
        for inhabitant in self.inhabitants:
            print(inhabitant)
    


habitat = Habitat("city", 18, None)

habitat.add_inhabitant(louie)
habitat.add_inhabitant(max)

habitat.print_inhabitants()