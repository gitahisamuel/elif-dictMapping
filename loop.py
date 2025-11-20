class Animal:
    def __init__(self, name, species):   # fixed: use __init__, not _init_
        self.name = name
        self.species = species

    def is_eating(self):
        print(f"{self.name} the {self.species} is eating 🍽️")

    def is_drinking(self):
        print(f"{self.name} the {self.species} is drinking 💧")

    def set_name(self, new_name):
        self.name = new_name

    def set_species(self, new_species):
        self.species = new_species

    def __str__(self):
        return f"{self.name} the {self.species}"


# Create a list of animals
animals = [
    Animal("Tom", "Cat"),
    Animal("Jerry", "Mouse"),
    Animal("Jack", "Bird"),
    Animal("King", "Fish")
]

# Behaviors: each animal eats and drinks
for animal in animals:
    animal.is_eating()
    animal.is_drinking()

print("\n--- Let's rename them to be more royal / cute ---")

# Update names in a fun way
for animal in animals:
    old_name = animal.name
    new_name = f"{old_name} Jr"  # make it “Jr” for fun
    animal.set_name(new_name)
    print(f"Renamed {old_name} → {animal}")

print("\n--- Final animal list ---")
for animal in animals:
    print(animal)
