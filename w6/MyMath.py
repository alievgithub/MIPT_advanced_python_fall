import math

class MyMath:
    __complex = False
    pi = 3.14

    @classmethod
    def get_name(cls):
        return cls.__name__

    @staticmethod
    def sin(x):
        return math.sin(x)

    @classmethod
    def get_complex(cls):
        return cls.__complex

print('Enter argument of sin(x): ', end = '')
x = float(input())

print('Result of', 'sin(' + str(x) + ') is', MyMath.sin(2))
print('Simple value of pi is', MyMath.pi)
print('Value of __complex is', MyMath.get_complex())
