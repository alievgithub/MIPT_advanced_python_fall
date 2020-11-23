import multiprocessing
import numpy as np

def dot(v1, v2):
    return np.dot(v1, v2)

v1 = [0, 1, 27, 10]
v2 = [3, 14, 5, 64]

pool = multiprocessing.Pool(processes = 4)
res = [pool.apply(dot, args = (i, j)) for i, j in zip(v1, v2)]

print(sum(res))
