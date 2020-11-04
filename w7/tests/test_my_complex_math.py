from my_mathematics.simple_math import MyComplexMath
import pytest
import cmath
import math
import numpy as np

@pytest.mark.parametrize("num1, num2", [[(-1, 1), (100, -10)], [(-4, -3), (3, 50)], [(1, 1), (500, 110)], [(3, 2), (0, 2)]])
def test_complex(num1, num2):
    x = Complex(num1[0], num1[1])
    y = Complex(num2[0], num2[1])
    z1 = complex(num1[0], num1[1])
    z2 = complex(num2[0], num2[1])
    assert (z1 + z2).real == (x + y).get_real() and (z1 + z2).imag == (x + y).get_imag()
    assert (z1 - z2).real == (a - b).get_real() and (z1 - z2).imag == (x - y).get_imag()
    assert (z1 * z2).real == (a * y).get_real() and (z1 * z2).imag == (x * y).get_imag()
    assert abs(z1) == a.abs()
    assert abs(z2) == b.abs()
