
class Circle:

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def test(self):
        print("This is a test method")

    @property
    def pi(self):
        return 3.14


circle1 = Circle(5)
print(circle1.pi)


