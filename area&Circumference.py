class Circle:
    pi = 3.14
    def __init__(self, radius):
        self.radius = radius

    def get_circumference(self):
        return 2 * self.pi * self.radius

    def get_area(self):
        return self.pi * self.radius*self.radius

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_area(self):
        return self.length*self.width



circle = Circle(4)
circum = circle.get_circumference()
area = circle.get_area()
print("Circumference : ", circum)
print("Area : ", area)

rectangle = Rectangle(5, 10)
area = rectangle.get_area()
print("Area of rectangle is :", area)