from abc import ABC , abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self,height,widths):
        self.height = height
        self.widths = widths

    def area(self):
        return self.height * self.widths
    
rect_1 : Rectangle = Rectangle(5,3)
print(f"Area of Rectangle : {rect_1.area()}")
        