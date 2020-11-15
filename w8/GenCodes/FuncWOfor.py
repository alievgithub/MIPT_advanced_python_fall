def print_map(function, iterable):
    iterator = iter(iterable)
    i = 0
    while i < len(iterable):
        print(function(next(iterator)))
        i += 1
'''
def sqrt(x):
    return x ** (1/2)

print(print_map(sqrt, [1, 2, 3, 4]))
'''
