import sys
sys.setrecursionlimit(10**7)

def dfs(now):
    global target
    if now not in maps:         # child가 없는 경우
        return 1
    child = maps[now]
    if check[child] == 0:       # 순환인 경우
        target = child
        check[now] = 1
    elif check[child] != -1:    # 이미 dfs를 끝낸 child
        check[now] = check[child] + 1
    else:                       # 방문한적 없는 child
        check[child] = 0
        check[now] = dfs(child) + 1
        if now == target:
            circle_dfs(now, target, check[now])
            target = -1

    return check[now]

def circle_dfs(now, tg, count):
    check[now] = count
    child = maps[now]
    if child == tg:
        return
    circle_dfs(child, tg, count)

m, n = map(int, input().split())
maps = {}   # 각 섬의 출구
for _ in range(m):
    f, t = map(int, input().split())
    maps[f] = t

target = -1
check = [-1 for _ in range(n)]  # check[i] = i번째 섬으로부터 갈 수 있는 최대 거리, -1인 경우 조사한적 없고, 0인 경우 조사는 했지만 거리가 미정인 경우
for i in range(n):
    if check[i] == -1:
        check[i] = 0
        check[i] = dfs(i)

print(max(check))

# 모든 섬에 대해 dfs 탐색을 한다.
# dfs는 섬 이동간의 순환이 일어났거나 출구가 없는 섬을 방문한 경우에 끝남.
# 1) 출구가 없는 경우 dfs를 거슬러 올라가며 check + 1을 저장
# 2) 순환이 발생한 경우 (조사는 했지만 거리를 지정하지 않은 경우를 check 리스트에 0으로 저장했으니 판별가능, dfs 중 check가 0인 child를 만난 경우)
#    순환 내의 모든 섬의 check를 순환하는 섬의 개수로 저장 (circle_dfs 사용)
# 이어지지 않은 섬은 check가 -1이므로 check가 -1인 모든 섬에 대해 dfs 적용
# 순환이 발생하더라도 모든 섬을 dfs하는데 O(n)시간 소요
# 딕셔너리를 구성할때 O(m)시간이 소요
# 따라서 O(n + m)시간 소요