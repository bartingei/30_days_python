class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def speak(self):
        return f"{self.name} makes a sound."

    def describe(self):
        return f"{self.name} is a {self.species}."

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Dog")
        self.breed = breed

    def speak(self):
        return f"{self.name} barks!"

    def fetch(self):
        return f"{self.name} fetches the ball."

# Example usage
if __name__ == "__main__":
    dog = Dog("Buddy", "Golden Retriever")
    print(dog.describe())
    print(dog.speak())
    print(dog.fetch())
