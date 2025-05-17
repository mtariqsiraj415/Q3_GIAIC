class Person:
    def __init__(self,name):
        self.name = name

class Teacther(Person):
    def __init__(self,name,subject):
        super().__init__(name)
        self.subject = subject


teachter : Teacther = Teacther("Sir Hamzah","Python")
print(f"Name : {teachter.name} ,  Subject : {teachter.subject}")
