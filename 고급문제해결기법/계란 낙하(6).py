E, F = map(int, input().split())
d = [[0] * (F + 1) for _ in range(E + 1)]

for i in range(1, E + 1):
    d[i][1] = 1
for i in range(1, F + 1):
    d[1][i] = i

maxV = 1001
minT = maxV
for i in range(2, E + 1):
    for T in range(2, F + 1):
        d[i][T] = d[i - 1][T - 1] + d[i][T - 1] + 1

        if d[i][T] >= F:
            minT = min(minT, T)

if minT != maxV:
    print(minT)
else:
    print(F)

# 모든 계란 수(i), 시행 수(T)에 대해 탐색하면서
# d[i][T]를 채우며 d[i][T]값이 F이상인 T값 중의 최소를 계산
# 만약 해당하는 T값이 없다면 F출력

# d[i][T]는 d[i][T - 1]와 d[i - 1][T - 1]의 상태에서만 발생하므로
# d[i][T - 1] : 같은 계란의 수로 하나 적은 시행을 한 상태의 최대 층
# d[i - 1][T - 1] : 계란이 하나 적고 시행횟수가 하나 적은 상태의 최대 층
# d[i][T] = d[i - 1][T - 1] + d[i][T - 1] + 1 라는 점화식이 세워짐

# E만큼 탐색, F만큼 탐색이 중첩되어 발생하므로
# 시간복잡도는 O(E * F)