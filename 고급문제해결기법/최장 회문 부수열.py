A = input()
n = len(A)
d = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

maxL = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if A[j - 1] == A[n - i]:
            temp = d[j - 1][i - 1] + 1
        else:
            temp = max(d[j - 1][i], d[j][i - 1])
        if maxL < temp:
            maxL = temp
        d[j][i] = temp

print(maxL)

# LCS의 길이를 구하기 위해 
# 
# 입력된 문자열 A를 뒤집어 A와의 공통 부수열은 회문이 됨
# 따라서 A와 뒤집힌 A의 LCS를 구한것이 답
# 공통 부수열의 길이를 구하기 위해 d를 다음과 같이 정의
# d[i][j] : A[0 ~ i]와 B[0 ~ j]의 부수열 길이의 최대값
# 모든 d에 대해 값을 채우며 현재 비교중인 값인 A[i]와 B[j]의 상태에 따라 값을 채움
# 1. A[i]가 B[j]와 같을때 : d[i - 1][j - 1]에 1을 더한 값
# 2. A[i]가 B[j]와 다를때 : d[i - 1][j] 또는 d[i][j - 1] 중 더 큰값
# n * n 크기의 리스트 d를 채우기때문에 시간복잡도는 O(n^2)