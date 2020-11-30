from itertools import groupby

def compress_string(s):
    keys = []
    groups = []
    for key, group in groupby(s):
        keys.append(int(key))
        groups.append(len(list(group)))

    return list(zip(groups, keys))

#print(compress_string('04102001'))
