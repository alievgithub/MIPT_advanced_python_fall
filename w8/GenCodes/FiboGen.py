def Fibo(n):
    def FiboGen():
        first = 0
        second = 1
        while True:
            yield first
            first, second = second, first + second

    f = FiboGen()
    for i in range(n):
        next(f)
    return next(f)

#print(Fibo(6))
