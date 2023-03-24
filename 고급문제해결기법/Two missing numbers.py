import math

def guess_two_missing_numbers(n, S, T):
	
	OS = n * (n + 1) / 2
	OT = n * (n + 1) * (2 * n + 1) / 6
	
	A = OS - S						# a + b
	B = OT - T						# a^2 + b^2
	C = A * A - B					# 2ab
	D = math.sqrt(B - C)	# b - a
	
	a = int((A - D) / 2)
	b = int((A + D) / 2)	
	
	return a, b  # a < b are two missing numbers

n = int(input())
S, T = [int(x) for x in input().split()]
a, b = guess_two_missing_numbers(n, S, T)
print(a, b)
