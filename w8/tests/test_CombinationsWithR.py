from GenCodes.CombinationsWithR import get_combinations_with_r
import pytest

def test_combinations_with_r():
    assert get_combinations_with_r('cat', 2) == ['aa', 'ac', 'at', 'cc', 'ct', 'tt']
    assert get_combinations_with_r('dog', 3) == ['ddd', 'ddg', 'ddo', 'dgg', 'dgo',
                                                 'doo', 'ggg', 'ggo', 'goo', 'ooo']
