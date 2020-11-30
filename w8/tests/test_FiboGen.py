from GenCodes.FiboGen import FiboGen
import pytest

def test_FiboGen():
    assert 5 == FiboGen(5)
    assert 1 == FiboGen(1)
