# ---------------------- 3:Public Variables and Methods ---------------------- #

class Car:
    def __init__(self,brand):
        self.brand = brand

    def start(self):
        return f"{self.brand} is starting."
    


car:Car = Car("Toyota")
print(car.brand)
print(car.start())

