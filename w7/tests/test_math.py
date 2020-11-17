from my_mathematics.math import MyMath
import math
import pytest

@pytest.mark.parametrize("value", [0, 1, 2, 3, 0.001, 5468, 3000, 4740, 4000, -4])
def test_math_sin(value):
    assert math.sin(value) == MyMath.sin(value)

@pytest.mark.parametrize("value", [0, 1, 2, 3, 4, 5, 0.01, 3e-7, 232, 213123, 392, 921])
def test_math_sqrt(value):
    assert math.sqrt(value) == MyMath.sqrt(value)
