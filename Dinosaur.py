class dinosaur:
    def __init__(self, name, species, diet, age) -> None:
        self.name = name
        self.species = species
        self.diet = diet
        self.age = age

#shows all info about dino
    def desplay_info(self):
        return f"{self.name} is a {self.species} it eats {', '.join(self.diet)} and is {self.age} years old."
    
#method for what it eats
    def eating(self):
        if self.diet == "meat":
            return f"{self.name} is a carnivourus dino"
        elif "meat" in self.diet and "plants" in self.diet:
            return f"{self.name} is an omnivore"
        else:
            return f"{self.name} is a herbavore"

    
#raooooorrrrrrrr
    def roar(self):
        return f"{self.name} is going ROOOOAAAAARRRRR"



dino1 = dinosaur("Rex", "Tyrannosaurus Rex", "meat", 12)
dino2 = dinosaur("Bob", "stegosaurus", "plants", 15)
dino3 = dinosaur("steven", "Deinocheirus", ["meat", "plants"], 7)


print(dino1.desplay_info())
print(dino1.eating())
print(dino2.desplay_info())
print(dino2.eating())
print(dino3.desplay_info())
print(dino3.eating())


