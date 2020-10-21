class AbstractFigure:

    def __init__(self, area, length):
        self.area = area
        self.length = length

    def print_self(self):
        print('Area is', self.area)
        print('Length', self.length)


class Triangle(AbstractFigure):

    static_field = 0

    def __init__(self, side1, side2, side3):
        self.static_field = 5
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def get_perimiter(self):
        return self.side1 + self.side2 + self.side3

    def get_area(self):
        p = self.get_perimiter() / 2
        return (p * (p - self.side1) * (p - self.side2) * (p - self.side3))**0.5

    def print_self(self):
        print('Side1:', self.side1)
        print('Side2:', self.side2)
        print('Side3:', self.side3)
        print('Area:', self.get_area())


#fig1 = AbstractFigure(2, 5)
#print(fig1.area)

#fig2 = AbstractFigure(9, 10)
#fig2.print_self()

tr1 = Triangle(3, 5, 3)
tr1.print_self()

print(tr1.get_area())
