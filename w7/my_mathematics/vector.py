import math
import numpy as np

class Vector:
    __x = 0
    __y = 0
    __z = 0
    __values = [__x, __y, __z]

    def __init__(self, *args):
        if type(args[0]) == str:
            self.__values = list(map(float, list(args[0].split(','))))
        else:
            self.__values = list(args)

    def __add__(self, other):
        added = list(a + b for a, b in zip(self, other))
        return Vector(*added)

    def __iter__(self):
        return self.__values.__iter__()

    def __sub__(self, other):
        subbed = list(a - b for a, b in zip(self, other))

    def length_of_vector(self):
        return math.sqrt(sum(value**2 for value in self.__values))

    def __and__(self, other):
        a = np.array(self.__values)
        b = np.array(other.__values)
        return np.cross(a, b)

    def scal_mul(self, other):
        return sum(a * b for a, b in zip(self, other))

    def __mul__(self, other):
        if type(other) == type(self):
            return self.scal_mul(other)
        elif type(other) == int or type(other) == float:
            product = list(a * other for a in self)
            return Vector(*product)

    def __str__(self):
        return f"[{self.__values[0]}, " + f"{self.__values[1]}, " + f"{self.__values[2]}]" + "\n"
