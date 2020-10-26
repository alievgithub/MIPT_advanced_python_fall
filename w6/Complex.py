class Complex(object):
    def __init__(self, real, imag = 0):
        self.__real = float(real)
        self.__imag = float(imag)

    def __str__(self):
        return "({}, {})".format(self.__real, self.__imag)

    def __add__(self, num):
        return Complex(self.__real + num.__real, self.__imag + num.__imag)

    def __sub__(self, num):
        return Complex(self.__real - num.__real, self.__imag - num.__imag)

    def __truediv__(self, num):
        denominator = num.__real ** 2 + num.__imag ** 2
        if denominator == 0:
            return None
        else:
            return Complex((self.__real * num.__real + self.__imag * num.__imag) / denominator, (self.__imag * num.__real + self.__real * num.__imag) / denominator)

    def __mul__(self, num):
        return Complex(self.__real * num.__real - self.__imag * num.__imag, self.__real * num.__imag - self.__imag * num.__real)

    def __neg__(self):
        return Complex(- self.__real, - self.__imag)

    def __abs__(self):
        return (self.__real ** 2 + self.__imag ** 2) ** (1/2)

    def __eq__(self, num):
        return self.__real == num.__real and self.__imag == num.__imag

if __name__ == '__main__':
    x = Complex(2, 4)
    y = Complex(3, 5)

    print('Two complex numbers:', x, y)
    print('Sum:', x + y)
    print('Subtraction:', x - y)
    print('Division:', x / y)
    print('Multiplication:', x * y)
    print('Negation:', - x, - y)
    print('Absolute:', abs(x), abs(y))
    print('Equality:', x == y)
