class Animals:
 
    
    def __init__(self, name , species):
        self.name = name
        self.species = species


    def isEating(self):
        print (f"{self.name} the {self.species} is eating")   

    def isDrinking(self):
        print(f"{self.name} the {self.species} is drinking")


    def setName(self, new_name):
        self.name = new_name
    def setSpecies(self, new_species):
        self.species = new_species


animalOne = Animals("Tom", "Cat")
animalOne.isEating()

animals = [
    Animals("Jerry", "Mouse"),
    Animals("Jack", "Bird"),
    Animals("King", "Fish")
]
for animal in animals:
    animal.isEating()
    animal.isDrinking()

for animal in animals:
    print(f"Old name: {animal.name}")
    print(f"New name: {animal.name}")


    
