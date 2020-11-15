from GenCodes.Combinations import get_combinations
import pytest

def test_combinations():
    assert get_combinations('cat', 2) == ['a', 'c', 't', 'ac', 'at', 'ct']
    assert get_combinations('dog', 3) == ['d', 'g', 'o', 'dg', 'do', 'go', 'dgo']
