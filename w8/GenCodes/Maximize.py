from itertools import accumulate

def maximize(lists, m):
    max_squared = [max(array) ** 2 for array in lists]
    res = [x for x in accumulate(max_squared)]

    return max([x % m for x in res])

"""
lists = [[1, 2], [3, 2, 6], [1, 2, 11, 3, 10]]
print(maximize(lists, m = 1000))
"""
