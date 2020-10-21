class Shape:
    def __init__(self, width, height):
        self.width = width
        self.height = height

class Triangle(Shape):
    def area(self):
         return self.width * self.height / 2

class Rectangle(Shape):
    def area(self):
         return self.width * self.height

print('Enter width and heigth through a space: ', end = '')
x, y = map(int, input().split())

print('Triangle area is ', Triangle(x, y).area())
print('Rectangle area is ', Rectangle(x, y).area())
