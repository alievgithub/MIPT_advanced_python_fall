'''
#2.1

def insert_sort(arr):
	N = len(arr)
	for top in range(1, N):
		k = top
		while k > 0 and arr[k - 1] > arr[k]:
			arr[k], arr[k - 1] = arr[k - 1], arr[k]
			k -= 1
			for i in range(N):
				print(arr[i], end = " ")
			print()
	if k > 0:
		return 1

line = input()
arr = []
N = 0
for x in line.split():
	x = int(x)
	arr.append(x)
if insert_sort(arr) == 1:
	for i in range(N):
		print(arr[i], end = " ")
	print()
'''
'''
#2.2

def bubble_sort(arr):
	i = 0
	N = len(arr)
	for bypass in range(1, N):
		for k in range(0, N - bypass):
				if arr[k] > arr[k + 1]:
					arr[k], arr[k + 1] = arr[k + 1], arr[k]
					for j in range(N):
						print(arr[j], end = " ")
					print()
	return 1

line = input()
arr = []
N = 0
for x in line.split():
	x = int(x)
	arr.append(x)
if bubble_sort(arr) == 1:
	for j in range(N):
		print(arr[j], end = " ")
	print()
'''
'''
#2.3

def fool_sort(arr):
	i = 0
	N = len(arr)
	while i < len(arr) - 1:
		if arr[i] > arr[i + 1]:
			arr[i], arr[i + 1] = arr[i + 1], arr[i]
			i=0
			for j in range(N):
				print(arr[j], end = " ")
			print()
			k=1
		else:
			i += 1
			k=0
	if k == 1:
		return 1

line = input()
arr = []
N = 0
for x in line.split():
	x = int(x)
	arr.append(x)
if fool_sort(arr) == 1:
	for j in range(N):
		print(arr[j], end = " ")
	print()
'''
