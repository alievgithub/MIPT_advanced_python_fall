import multiprocessing
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

def dot(v1, v2):
    return np.dot(v1, v2)

def proc_dot(mas, proc):
    pool = multiprocessing.Pool(processes = proc)
    res = [pool.apply(dot, args = (sub1, sub2,))
               for sub1, sub2 in split(mas[0], mas[1], proc)]

    return res

def split(v1, v2, num):
    res1, res2 = np.split(v1, num), np.split(v2, num)
    for i in range(len(res1)):
        if res1[i].size > 0:
            yield (res1[i], res2[i])

if __name__ == "__main__":
    length = int(1e4)
    vectors = [np.random.randn(length), np.random.randn(length)]
    x = [2, 2, 5, 8, 10]
    res = []
    for processes in x:
        tmp = []
        for sample in range(3):
            start = datetime.now()
            print(proc_dot(vectors, processes))
            tmp.append((datetime.now() - start).microseconds)
        res.append(sum(tmp) / len(tmp))
    plt.plot(x, res)
    plt.grid()
    plt.ylabel("Time [ms]")
    plt.xlabel("Quantity")
    plt.show()
