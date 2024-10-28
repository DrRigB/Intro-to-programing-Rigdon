class Animal:
    def __init__(self, name, habbitat, sound):
        self.name = name
        self.habbitat = habbitat
        self.sound = sound
    
    def get_name(self):
        return self.name

    def get_habbitat(self):
        return self.habbitat
    
    def speak(self):
        return f"{self.name} makes a sound: {self.sound}"

class Cat(Animal):
    def __init__(self, name, habbitat):
        
        super().__init__(name, habbitat, "Meow")

    def speak(self):
        return f"{self.get_name()} says: {self.sound} loudly in {self.get_habbitat()}"

    def climb(self):
        return f"{self.get_name()} is climbing a tree!"




class Carson(Animal):
    def __init__(self, name, habbitat, sound):
        super().__init__(name, habbitat, sound)


    def speak(self):
        return f"{self.get_name()} is saying some silly things"
    

    def shortness(self):
        return f"{self.get_name()} is very short"

def main():
    # Create Dog and Cat objects
    carson = Carson("Carson", "the backyard", "Talk")
    clyde = Cat("Clyde", "the living room")


    # Call the speak method on each object
    print(carson.speak())      # Demonstrates polymorphism in the Dog class
    print(carson.shortness())       # Dog-specific behavior


    print(clyde.speak())    # Demonstrates polymorphism in the Cat class
    print(clyde.climb())    # Cat-specific behavior


# Run the main function
if __name__ == "__main__":
    main()

