'''
#1.1

from math import sqrt

sumall = sumsquare = q = 0
min = 999999
max = -999999
A = []
while 1:
    x = input()
    if x != 'End':
        x = int(x)
        A.append(x)
        sumall += x
        q += 1
        min = x if x < min else min
        max = x if x > max else max
    else:
        break
average = sumall / q;
for i in range(q):
    sumsquare += (A[i] - average)**2
rms = sqrt(sumsquare / q)
print(max)
print(min)
print(average)
print(rms)
'''
'''
#1.2

from math import sqrt

sumall = sumsquare = q = 0
min = 999999
max = -999999
A = []
while 1:
    x = input()
    if x != 'End':
        x = int(x)
        sumall += x
        sumsquare += x**2
        q += 1
        min = x if x < min else min
        max = x if x > max else max
    else:
        break
average = sumall / q;
rms = sqrt(sumsquare / q - ((sumall / q)**2))
print(max)
print(min)
print(average)
print(rms)
'''
