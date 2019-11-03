class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.radius ** 2 * 3.14

    def perimeter(self):
        return (self.radius * 2) * 3.14


circle1 = Circle(radius=1)
print(circle1.area())
print(circle1.perimeter())

circle3 = Circle(radius=3)
print(circle3.area())
print(circle3.perimeter())
