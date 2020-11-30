from itertools import combinations

def get_combinations(s, n):
    comb = sorted(["".join(sorted(x)) for i in range(1, n + 1) for x in combinations(s, i)])
    comb.sort(key = lambda x: len(x))
    return comb

#print(get_combinations("Artem", 2))
