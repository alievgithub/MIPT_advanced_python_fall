from GenCodes.Compress import compress_string
import pytest

def test_compress_string():
    assert compress_string('1222311') == [(1, 1), (3, 2), (1, 3), (2, 1)]
    assert compress_string('12223111') == [(1, 1), (3, 2), (1, 3), (3, 1)]
