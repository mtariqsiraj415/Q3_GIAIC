class Dog:
    def __init__(self,name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        return (f"{self.name} says wooofff!")

dog_1:Dog = Dog("Tommy","Labradar")
print(dog_1.bark())