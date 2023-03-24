def solve(A):
	n = len(A)
	if n:
		A.sort()	# O(nlogn)
		s = 1
		e = n - 1 - ((n + 1) % 2)	# n이 홀수일때는 e의 값이 n - 1부터, 짝수일때는 e의 값이 n - 2 부터 시작
		while s < e:	# O(n)
			A[e], A[s] = A[s], A[e]
			s += 2
			e -= 2
	return A

# 주어진 리스트를 정렬하고 O(nlogn)
# 정렬된 리스트를 탐색하며 O(n) A[s]와 A[e]를 비교를 하니
# O(nlogn) + O(n) = O(nlogn)

def check(B):
	if not (B[0] <= B[1]): return False
	for i in range(1, len(B)-1):
		if i%2 == 1 and not (B[i] >= B[i+1]):
			return False
		if i%2 == 0 and not (B[i] <= B[i+1]):
			return False
	return True		
	
A = [int(x) for x in input().split()]
B = solve(A)
print(check(B))
