def reconstruct(S, L):
	n = len(S)
	A = [0 for _ in range(n)]
	for i in range(n):
		front = S[i] + ((n - i) - L[i])
		A[i] = front - 1
	return A
	
# S와 L을 차례로 읽어들임
S = [int(x) for x in input().split()]
L = [int(x) for x in input().split()]
A = reconstruct(S, L)
print(A)

# 리스트 A를 i를 기준으로 나누면
# A[ : i]와 A[i], A[i + 1 : ]가 발생한다
# B = A[ : i], C = A[i + 1 : ]라고 하면
# B의 길이는 i, C의 길이는 n - i
# B의 길이는 A[i]보다 작은 수 S[i]개와 나머지(A[i]보다 큰 수)의 합으로 구성
# C의 길이는 A[i]보다 큰 수 L[i]개와 나머지(A[i]보다 작은 수)의 합으로 구성
# 결국 전체 A에서 S[i]의 값과 C 중에 L[i]가 아닌 개수를 더하면 A[i]가 리스트에서 몇번째로 큰 값인지 알 수 있음
# A[i]보다 작은 수의 개수는 S[i] + ((n - i) - L[i]) 이라는 결론
# 순열이 0부터 시작하니 이 값에 -1를 한 수가 A[i]에 채워짐
# 시간복잡도는 O(n)