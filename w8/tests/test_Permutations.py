from GenCodes.Permutations import get_permutations
import pytest

def test_permutations():
    assert get_permutations('cat', 2) == ['ac', 'at', 'ca', 'ct', 'ta', 'tc']
    assert get_permutations('dog', 1) == ['d', 'g', 'o']
