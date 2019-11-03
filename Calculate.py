class Circle:
    def __int__(self, radius):
        self.area = (radius ** 2 * 3.14) / 2

        self.perimeter = (radius * 2) * 3.14


circle1 = Circle(radius=1)
print(circle1.area)
print(circle1.perimeter)
