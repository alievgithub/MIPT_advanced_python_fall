'''
#1.1 Extra

A = [1, 2, 3, 4, 1]

ENUM = []
NEW = []

for i in enumerate(A):
    ENUM.append(i)
for i in range(ENUM[-1][0] + 1):
    NEW.append(A[i] + A[-i - 1])
    if i >= (ENUM[-1][0] + 1) / 2 - 1:
        break

print(*NEW)
'''
'''
#1.2 Extra

A = [1, 2, 3, 4, 1, 1]

NEW = []

while A != []:
    NEW.append(A[0] + A[-1])
    A.pop()
    if A != []:
        A.pop(0)

print(*NEW)
'''
