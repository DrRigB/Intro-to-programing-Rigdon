import pdb

class Character:
    def __init__(self, name, element):
        self.name = name
        self.element = element

    def introduce(self):
        return f"my name is {self.name} and I am a {self.element} bender!"
    


aang = Character("Aang", "Air")
katara = Character("Katara", "Water")
toph = Character("Toph", "Earth")
zuko = Character("Zuko", "Fire")

def journey_to_element(character):
    if character.element == "Air":
        return "Aang flies with his glider."
    
    elif character.element == "Water":
        return "Katara bends water to travel."
    elif character.element == "Earth":
        return "Toph creates earth walls to move forward."
    elif character.element == "Fire":
        return "Zuko uses fire to fly around."
    
    else:
        return "This person can't bend elements!"
#pdb.set_trace() 
print(aang.introduce())
print(journey_to_element(aang))
print(katara.introduce())
print(journey_to_element(katara))
print(toph.introduce())
print(journey_to_element(toph))
print(journey_to_element(zuko))
print(zuko.introduce())