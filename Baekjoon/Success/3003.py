stand = [1, 1, 2, 2, 2, 8]

input = list(map(int, input().split()))

for i, j in zip(stand, input):
	print(i - j, end = ' ')