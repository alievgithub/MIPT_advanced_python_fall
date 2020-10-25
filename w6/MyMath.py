import math
import cmath

class MyMath:
    _complex = False # Инкапсуляция
    pi = 3.14

    @classmethod
    def get_name(cls):
        return cls.__name__ # Инкапсуляция

    @staticmethod
    def sin(x):
        return math.sin(x)

    @classmethod
    def get_complex(cls):
        return cls._complex # Инкапсуляция

    @classmethod
    def sqrt(cls, x):
        cres = cmath.sqrt(x)
        if x >= 0:
            return math.sqrt(x)
        else:
            if cls.get_complex(): # Полиморфизм
                return cres.real, cres.imag
            else:
                raise ValueError('You are working with real numbers')

class MyComplexMath(MyMath): # Наследование
    _complex = True # Инкапсуляция

"""
Мы использовали classmethod, а не staticmethod,
потому что в первом мы можем изменять его,
а в staticmethod вносить изменения будет невозможно
"""

print('Enter argument of sqrt(x): ', end = '')
x = float(input())

print('When _complex = True:', MyComplexMath.sqrt(x))
print('When _complex = False: ', end = '')
print(MyMath.sqrt(x))

'''
print('Enter argument of sin(x): ', end = '')
x = float(input())

print('Result of', 'sin(' + str(x) + ') is', MyComplexMath.sin(2))
print('Simple value of pi is', MyMath.pi)
print('Value of __complex is', MyMath.get_complex())
'''
