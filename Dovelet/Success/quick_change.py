c = int(input())

changes = [(25, 'QUARTER(S)'), (10, 'DIME(S)'), (5, 'NICKEL(S)'), (1, 'PENNY(S)')]
counts = [0 for _ in changes]

now = c
for idx, (i, t) in enumerate(changes):
	while now >= i:
		now -= i
		counts[idx] += 1

for idx, (i, t) in enumerate(changes):
	if idx != len(changes) - 1:
		print(str(counts[idx]) + ' ' + t + ', ', end = '')
	else:
		print(str(counts[idx]) + ' ' + t)