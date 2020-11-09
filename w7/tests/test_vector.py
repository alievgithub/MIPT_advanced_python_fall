from my_mathematics.vector import Vector
import pytest
import numpy as np

@pytest.mark.parametrize("vector1, vector2", [([1, 3, 5], [2, 3, 5]), ([0, 0, 0], [0, 0, 0]), ([-1, -2, -3], [1, 2, 3]),
                                              ([100, 100, 0], [0, 4, 5]), ([0, 100, 100], [2, 34, 5]),
                                              ([-100, 0, 100], [2, 43, 5]), ([100, 0, 100], [0, 0, 0])])
def test_vector_nums(vector1, vector2):
    np_vector1 = np.array(vector1)
    np_vector2 = np.array(vector2)
    x = np.array([vector2, vector1])
    assert np_vector1.dot(np_vector2) == Vector(*vector1) * Vector(*vector2)
    assert list(np.sum([np_vector1, np_vector2], axis=0)) == list(Vector(*vector1) + Vector(*vector2))
    assert np.diff(x, axis=0).any() == np.array(list(Vector(*vector1) - Vector(*vector2))).any()
    assert np.cross(np_vector1, np_vector2).tolist() == list(Vector(*vector1) & Vector(*vector2))
    assert np.linalg.norm(vector1) == Vector(*vector1).length_of_vector()
    assert np.linalg.norm(vector2) == Vector(*vector2).length_of_vector()


@pytest.mark.parametrize("vector1, vector2", [('1, 3, 5', '2, 3, 5'), ('0, 0, 0', '0, 0, 0'), ('-1, -2, -3', '1, 2, 3'),
                                              ('100, 100, 0', '0, 4, 5'), ('0, 100, 100', '2, 34, 5'),
                                              ('-100, 0, 100', '2, 43, 5'), ('100, 0, 100', '0, 0, 0')])
def test_vector_str(vector1, vector2):
    vector1 = list(map(float, list(vector1.split(','))))
    vector2 = list(map(float, list(vector2.split(','))))
    np_vector1 = np.array(vector1)
    np_vector2 = np.array(vector2)
    x = np.array([vector2, vector1])
    assert np_vector1.dot(np_vector2) == Vector(*vector1) * Vector(*vector2)
    assert list(np.sum([np_vector1, np_vector2], axis=0)) == list(Vector(*vector1) + Vector(*vector2))
    assert np.diff(x, axis=0).any() == np.array(list(Vector(*vector1) - Vector(*vector2))).any()
    assert np.cross(np_vector1, np_vector2).tolist() == list(Vector(*vector1) & Vector(*vector2))
    assert np.linalg.norm(vector1) == Vector(*vector1).length_of_vector()
    assert np.linalg.norm(vector2) == Vector(*vector2).length_of_vector()
