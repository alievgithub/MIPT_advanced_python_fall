def zip_analog(*iters):
    iterables = [iter(it) for it in iters]

    while True:
        res = []
        try:
            for it in iterables:
                res.append(next(it))
            yield tuple(res)
        except Exception:
            break

def map_analog(func, iter):
    for item in iter:
        yield func(item)

def enumerate_analog(seq):
    i = 0
    for item in seq:
        yield i, item
        i += 1

"""
print("Result for map:")
for i in map_analog(lambda x: x ** 2, [1, 2, 3, 4, 5]):
    print(i)

print("\nResult for enumerate:")
for ind, i in enumerate_analog([1, 2, 3, 4, 5]):
    print(f"ind - {ind}; element - {i}")

print("\nResult for zip: ")
for i, j, k in zip_analog([1, 2, 3, 4], [3, 4, 5, 6], [35, 45, 45]):
    print(i, j, k, sep='  ')
"""
