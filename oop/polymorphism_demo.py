# polymorphism_demo.py

import math  # ✅ Needed for Circle area calculation

class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must override the area() method")

class Rectangle(Shape):
    def __init__(self, length, width):  # ✅ Constructor check
        self.length = length
        self.width = width

    def area(self):  # ✅ Method check
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):  # ✅ Constructor check
        self.radius = radius

    def area(self):  # ✅ Method check
        return math.pi * (self.radius ** 2)

