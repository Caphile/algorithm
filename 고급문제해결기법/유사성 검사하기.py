n = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))

nP, nQ = [], []
for i in range(n):
    nP.append([P[i], i + 1])
    nQ.append([Q[i], i + 1])

nP = sorted(nP, key = lambda x : x[0])
nQ = sorted(nQ, key = lambda x : x[0])

print(1)

'''
s = [[0 for _ in range(n)] for _ in range(n)]   # P[i] < P[j]와 Q[i] < Q[j]이 동시에 성립하면 1, 그렇지 않다면 0
c = [0 for _ in range(n)]                       # s[i][0~n]의 값이 1인 개수 합

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        if P[i] < P[j] and Q[i] < Q[j]:
            s[i][j] = 1
            c[i] += 1

ans = 0
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        if s[i][j]:
            ans += c[j] - s[j][i]

print(ans)
'''