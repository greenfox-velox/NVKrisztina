class Circle:

    def __init__ (self, r):
        self.r = r

    def get_circumference(self):
        x = 2 * self.r * 3.141
        return x

    def get_area(self):
        y = (self.r ** 2) * 3.141
        return y

circle1 = Circle(10)

print(circle1.get_circumference())
print(circle1.get_area())

circle2 = Circle(5)

print(circle2.get_circumference())
print(circle2.get_area())
