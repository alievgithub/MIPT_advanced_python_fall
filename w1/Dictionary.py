#3

dict1 = {'A': 1, 'B': 2, 'C': 3}
# (2 вариант)
#dict2 = dict([(value, key) for (key, value) in zip(dict1.keys(), dict1.values())])
dict2 = {value: key for key, value in dict1.items()}
# (1 вариант) 
#for key, value in dict1.items():
#    dict2[value] = key
print(dict2)
