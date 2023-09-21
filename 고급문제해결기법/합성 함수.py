def dfs(now):
    global target
    if now not in maps:        # child가 없는 경우
        return 1
    child = maps[now]
    if leng[child] == 0:       # 순환인 경우
        target = child
        leng[now] = 1
    elif leng[child] != -1:    # 이미 dfs를 끝낸 child
        leng[now] = leng[child] + 1
    else:                       # 방문한적 없는 child
        leng[child] = 0
        leng[now] = dfs(child) + 1
        if now == target:
            
            target = -1

    return leng[now]

n = int(input())

maps = {}
values = list(map(int, input().split()))
for c, v in enumerate(values):
    maps[c + 1] = v

leaf = [-1 for _ in range(n + 1)]   # 각 노드의 순환 사이클 진입 전 마지막 노드
leng = [-1 for _ in range(n + 1)]   # 각 노드의 leaf 까지의 거리
ends = [[] for _ in range(n + 1)]   # 각 leaf에서 각 root 까지 경로 상의 모든 노드
cycle = []

target = -1
for i in range(1, n + 1):
    if leaf[i] == -1:
        leng[i] = dfs(i)

q = int(input())
for _ in range(q):
    x, k = map(int, input().split())

    now = x
    while k > 0:
        now = maps[now]
        k -= 1
    print(now)



# 각 노드의 끝 노드, 거리 (순환하지 않는다면)
# 각 끝 노드부터 각 노드까지의 거리
# 순환 내의 노드 처리