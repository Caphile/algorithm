import sys
sys.setrecursionlimit(10000)

class node:
    def __init__(self, now):
        self.p = []
        self.n = now
        self.c = []
        self.dept = 0

def dfs(now, d):
    now.dept = d
    while 1:
        a = len(now.p)
        if not a:
            break
        b = len(nodes[now.p[-1]].p)
        if a > b:
            break
        now.p.append(nodes[now.p[a - 1]].p[a - 1])
    for n in now.c:
        dfs(nodes[n], d + 1)

def maxSQ(num):
    i = 0
    while 2**i <= num:
        i += 1
    return i - 1

n, q = map(int, input().split())

nodes = [0]
for i in range(1, n + 1):
    nodes.append(node(i)) 

for _ in range(n - 1):
    p, c = map(int, input().split())
    nodes[p].c.append(c)
    nodes[c].p.append(p)

dfs(nodes[1], 1)

ans = []
for _ in range(q):
    u, v = map(int, input().split())

    # 항상 v의 깊이가 더 깊음
    if nodes[u].dept > nodes[v].dept:
        u, v = v, u

    # v의 깊이를 u와 같게 설정
    while 1:
        diff = nodes[v].dept - nodes[u].dept
        if not diff:
            break
        v = nodes[v].p[maxSQ(diff)]
    while 1:
        if u == v or nodes[u].p == []:
            ans.append(u)
            break
        u = nodes[u].p[0]
        v = nodes[v].p[0]

for a in ans:
    print(a)

# 각 노드의 정보를 class로 nodes 리스트에 저장 O(n)
# 구성된 트리를 돌며 깊이를 저장 O(n)
# 각 노드에 저장된 정보를 기반으로 2^n 번째 부모 노드를 저장 O(nlogn)
# 한 질의당 다음의 과정을 거침 O(logn)
# 1. v와 u의 깊이를 같게함 O(logn)
# 2. root로 향하며 조상을 찾는데 O(logn) 
# 한 질의당 O(logn) 시간 소요되므로
# 시간복잡도는 O((n+q)logn)