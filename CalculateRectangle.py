import math


class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width

    def diagonal(self):
        cal = math.sqrt(self.height ** 2 + self.width ** 2)
        return f'{cal:.2f}'


rectangle1 = Rectangle(height=5, width=6)
print(rectangle1.area())
print(rectangle1.diagonal())

rectangle2 = Rectangle(height=3, width=3)
print(rectangle2.area())
print(rectangle2.diagonal())
