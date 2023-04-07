E, F = map(int, input().split())
d = [i for i in range(F + 1)]

maxV = 1001
minT = maxV
for i in range(2, E + 1):
    now = [0, 1]
    for T in range(2, F + 1):
        now.append(now[T - 1] + d[T - 1] + 1)

        if now[T] >= F:
            minT = min(minT, T)

    d = now

if minT != maxV:
    print(minT)
else:
    print(F)

# 모든 계란 수(i), 시행 수(T)에 대해 탐색하면서
# d[T]를 채우며 d[T]값이 F이상인 T값 중의 최소를 계산
# 만약 해당하는 T값이 없다면 F출력

# 계란낙하(6)의 알고리즘에서 이차원리스트 d를 일차원으로 줄인 알고리즘
# 계란낙하(6)의 알고리즘의 점화식 : d[i][T] = d[i - 1][T - 1] + d[i][T - 1] + 1
# 위 점화식은 결국 현재상태인 i와 직전상태인 i - 1만 참조하므로
# 일차원 리스트 두개가 있다면 한개는 현재상태 i, 다른 한개는 직전상태인 i - 1를 저장
# 현재상태 리스트를 채우면 직전상태 리스트를 비운 후, 다음 상태(i + 1)를 저장하는것을 반복

# E만큼 탐색, F만큼 탐색이 중첩되어 발생하므로
# 시간복잡도는 O(E * F)