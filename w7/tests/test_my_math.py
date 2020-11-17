from my_mathematics.math import MyMath
import math
import pytest

@pytest.mark.parametrize("value", [0, 1, 2, 3, 0.001, 5468, -75, 3000, 4740, 4000])
def test_math_sin(value):
    assert math.sin(value) == MyMath.sin(value)
