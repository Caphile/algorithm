E, F = map(int, input().split())
d = [[0] * (F + 1) for _ in range(E + 1)]

for i in range(1, E + 1):
    d[i][1] = 1
for i in range(1, F + 1):
    d[1][i] = i

for i in range(2, E + 1):
    for j in range(2, F + 1):
        minT = 1000 # (E = i, F = j)인 상황에서 모든 x층의 d값중 최소 
        l, r = 1, j
        while l <= r:
            x = (l + r) // 2

            go_up = d[i][j - x]     # x층에서 계란 안깨짐
            go_do = d[i - 1][x - 1] # x층에서 계란 깨짐

            nowT = max(go_up, go_do) + 1
            minT = min(minT, nowT)

            if go_do < go_up:
                l = x + 1
            else:
                r = x - 1
        d[i][j] = minT

print(d[E][F])

# 모든 계란 수(i), 층 수(j)에 대해 탐색하면서
# 계란을 떨어트릴수 있는 모든 층x(1 ~ j)에 대해 d값의 최소를 계산
# 계란이 깨진다면 d[i - 1][x - 1]의 값, 계란이 깨지지 않는다면 d[i][j - x]의 값
# 단, 모든 층x를 하나씩 보는것보다 시간을 단축하기 위해 이진탐색을 활용
# 최악의 경우를 생각해야 하므로 둘 중 큰 값에 1을 더한 값을 현재 x층의 d값으로 저장
# E만큼 탐색, F만큼 탐색, logF만큼 탐색이 중첩되어 발생하므로
# 시간복잡도는 O(E * FlogF)