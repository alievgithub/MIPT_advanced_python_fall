import numpy as np
import threading
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

def dot(v1, v2):
    return np.dot(v1, v2)

def threaded_dot(mas, th):
    threads = []
    for sub1, sub2 in split(mas[0], mas[1], thread):
        threads.append(threading.Thread(target = dot, args = (sub1, sub2,)))
        threads[-1].start()

    for thread_t in threads:
        thread_t.join(timeout = 10)

    return "Completed"

def split(v1, v2, num):
    res1, res2 = np.split(v1, num), np.split(v2, num)
    for i in range(len(res1)):
        if res1[i].size > 0:
            yield (res1[i], res2[i])

if __name__ == "__main__":
    length = int(1e5)
    vectors = [np.random.randn(length), np.random.randn(length)]
    x = [2, 2, 5, 8, 10]
    res = []
    for thread in x:
        tmp = []
        for sample in range(3):
            start = datetime.now()
            print(threaded_dot(vectors, thread))
            tmp.append((datetime.now() - start).microseconds)
        res.append(sum(tmp) / len(tmp))
    plt.plot(x, res)
    plt.grid()
    plt.ylabel("Time [ms]")
    plt.xlabel("Quantity")
    plt.show()
