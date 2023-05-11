class node:
    def __init__(self, now):
        self.n = now
        self.c = []
        self.idx = 0
        self.cost = 0
        self.subs = 0

def preorder(now):
    pre.append(now.n) 
    for n in now.c:
        subs[now.n] += preorder(nodes[n])
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
nodes = [0]
for i in range(1, n + 1):
    nodes.append(node(i)) 
    nodes[i].cost = costs[i - 1]
for _ in range(n - 1):
    p, c = map(int, input().split())
    nodes[p].c.append(c)

pre = [0]
subs = [0] + [1 for _ in range(n)]
preorder(nodes[1])

idx = [0 for _ in range(n + 1)]
for i in range(1, n + 1):
    nodes[pre[i]].idx = i
    nodes[i].subs = subs[i] - 1

m = 2**(n - 1).bit_length()
bit = [0 for _ in range(m + 1)]
for i in range(1, n + 1):
    bit[i] += nodes[pre[i]].cost
    j = i + (i & -i)
    if j <= m:
        bit[j] += bit[i]

for _ in range(q):
    order = list(input().split())
    nd = int(order[1])
    if order[0] == 'subtree':
        print(preSum(nodes[nd].idx + nodes[nd].subs) - preSum(nodes[nd].idx - 1))
    elif order[0] == 'update':
        value = int(order[2])
        nodes[nd].value = value
        update(nodes[nd].idx, nodes[nd].value)