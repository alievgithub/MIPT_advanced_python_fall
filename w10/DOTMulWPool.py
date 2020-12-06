if __name__ == "__main__":
    import multiprocessing
    import numpy as np

    def dot(v1, v2):
        return np.dot(v1, v2)

    a, b = [i*2 for i in range(10)], [i for i in range(10)]

    pool = multiprocessing.Pool(processes = 4)
    res = [pool.apply(dot, args = (i, j)) for i, j in zip(a, b)]

    #print(sum(res))
