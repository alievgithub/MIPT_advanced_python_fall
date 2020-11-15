from GenCodes.AnalogFuncs import zip_analog, map_analog, enumerate_analog
import numpy as np
import pytest

def test_zip():
    a = ['a', 'b', 'c', 'd']
    b = [1, 2, 3, 4]
    c = (1, 2, 4, 5)
    for pair in zip(zip_analog(a, b, c), zip(a, b, c)):
        assert pair[0] == pair[1]

def test_map():
    func = np.cos
    iter1 = [1, 2, 3]
    iter2 = (1, 2, 3)
    for iter in [iter1, iter2]:
        for pair in zip(map_analog(func, iter), map(func, iter)):
            assert pair[0] == pair[1]

def test_enumerate():
    arr1 = [10, 12, 13, 14]
    arr2 = ['a', 'b', 'c']
    for arr in [arr1,arr2]:
        for pair in zip(enumerate_analog(arr), enumerate(arr)):
            assert pair[0] == pair[1]
