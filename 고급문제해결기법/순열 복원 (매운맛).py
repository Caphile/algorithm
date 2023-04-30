def reconstruct(B):
    n = len(B)
    A = [0 for _ in range(n)]
    check = [i for i in range(n)]
    for i in range(n - 1, -1, -1):
        A[i] = check.pop(B[i])
    return A

B = [int(x) for x in input().split()]
A = reconstruct(B)
print(A)

# check 리스트에 리스트 A에 채워야 하는 값들을 저장하고 A를 채울때마다 해당 값을 check에서 pop O(n)
# 항상 A의 채워지지 않은 마지막 인덱스부터 값을 채우면
# check 리스트에서 남아있는 값들 중 B[i]번째의 값을 가지게 됨을 알 수 있음