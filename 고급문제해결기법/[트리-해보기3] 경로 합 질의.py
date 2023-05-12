class node:
    def __init__(self, now):
        self.n = now
        self.p = 0
        self.c = []
        self.idx = 0
        self.cost = 0
        self.subs = 0
        self.diff = 0
        self.sum = 0

def preorder(now, cost):
    pre.append(now.n) 
    now.sum = cost
    for n in now.c:
        subs[now.n] +=  preorder(nodes[n], nodes[n].cost + cost)
    return subs[now.n]

def update(i, v):
    global m
    while i <= m:
        bit[i] += v
        i += i & -i

def preSum(i):
    ps = 0
    while i > 0:
        ps += bit[i]
        i -= i & -i
    return ps

n, q = map(int, input().split())

costs = list(map(int, input().split()))
nodes = [node(0)]
for i in range(1, n + 1):
    nodes.append(node(i)) 
    nodes[i].cost = costs[i - 1]
for _ in range(n - 1):
    p, c = map(int, input().split())
    nodes[p].c.append(c)

pre = [0]
subs = [0] + [1 for _ in range(n)]
preorder(nodes[1], nodes[1].cost)

idx = [0 for _ in range(n + 1)]
for i in range(1, n + 1):
    nodes[pre[i]].idx = i
    nodes[i].subs = subs[i]

for i in range(1, n + 1):
    nodes[pre[i]].diff = nodes[pre[i]].sum - nodes[pre[i - 1]].sum

m = 2**(n - 1).bit_length()
bit = [0 for _ in range(m + 1)]
for i in range(1, n + 1):
    bit[i] += nodes[pre[i]].diff
    j = i + (i & -i)
    if j <= m:
        bit[j] += bit[i]

for _ in range(q):
    order = list(input().split())
    nd = int(order[1])
    if order[0] == 'sum':
        print(preSum(nodes[nd].idx))
    elif order[0] == 'update':
        value = int(order[2])
        update(nodes[nd].idx, value)
        update(nodes[nd].idx + nodes[nd].subs, -value)

# 각 노드의 정보를 class로 nodes 리스트에 저장 
# preorder로 탐색했을때 방문하는 노드번호를 저장하는 pre 리스트를 구함
# preorder로 탐색함과 동시에 부트리의 노드 개수와 pathSum을 구함
# pre순서대로 나열된 node들간의 차를 각 node의 diff에 저장한 뒤,
# diff값이 업데이트 될 수 있으므로 diff를 BIT 자료구조로 저장함 O(nlogn)
# 한 질의당 두번의 업데이트 쿼리에 O(logn) 시간 소요되고
# diff의 prefixSum을 구하는데 O(logn)시간 걸리므로
# 시간복잡도는 O(nlogn)