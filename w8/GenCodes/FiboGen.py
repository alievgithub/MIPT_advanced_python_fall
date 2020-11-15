def FiboGen(n):
    def Fibo():
        first = 0
        second = 1
        while True:
            yield first
            first, second = second, first + second

    f = Fibo()
    for i in range(n):
        next(f)
    return next(f)

#print(FiboGen(6))
