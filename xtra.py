class Animals:
    def _init_(self, name, species):
        self.name = name
        self.species = species

    # Behaviors
    def isEating(self):
        print(f"{self.name} the {self.species} is eating")

    def isDrinking(self):
        print(f"{self.name} the {self.species} is drinking")

    # Setter methods
    def setName(self, new_name):
        self.name = new_name

    def setSpecies(self, new_species):
        self.species = new_species


animalOne = Animals("Tom", "Cat")
animalOne.isEating()

# Change name and species using setters
animalOne.setName("Tommy")
animalOne.setSpecies("Wild Cat")

print(animalOne.name)     
print(animalOne.species)  

#Loop
animals = [
    Animals("Jerry", "Mouse"),
    Animals("Jack", "Bird"),
    Animals("King", "Fish")
]

# Behaviors
for animal in animals:
    animal.isEating()
    animal.isDrinking()

# Update names
for animal in animals:
    print(f"Old name: {animal.name}")
    
    # change name using setter
    animal.setName(animal.name + " Jr")

    print(f"New name: {animal.name}")