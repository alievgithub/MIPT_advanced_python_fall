import numpy as np

class Average(Exception):
    pass

class Dispersion(Exception):
    pass

class Number(Exception):
    pass

def Processing():
    arr = []
    while True:
        try:
            x = yield
            arr.append(x)
            average = np.mean(arr)
            dispersion = np.var(arr)
            n = len(arr)
        except Dispersion:
            yield dispersion
        except Average:
            yield average
        except Number:
            yield n

if __name__ == "__main__":
    coroutine = Processing()
    next(coroutine)
    
    for i in range(20):
        coroutine.send(i)
        if i % 2 == 0:
            print("Average:", coroutine.throw(Average))
            next(coroutine)
        if i % 3 == 0:
            print("Dispersion:", coroutine.throw(Dispersion))
            next(coroutine)
        if i % 4 == 0:
            print("Number:", coroutine.throw(Number))
            next(coroutine)

    print("")
    print(coroutine.throw(Average))
    next(coroutine)

    print(coroutine.throw(Dispersion))
    next(coroutine)

    print(coroutine.throw(Number))
    next(coroutine)

    coroutine.close()
