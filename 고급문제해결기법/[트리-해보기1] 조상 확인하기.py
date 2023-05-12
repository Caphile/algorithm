import sys
sys.setrecursionlimit(10000)

class node:
    def __init__(self, now):
        self.n = now
        self.c = []

def preorder(now):
    global ord
    pre[now.n] = ord
    ord += 1
    for n in now.c:
        preorder(nodes[n])

def postorder(now):
    global ord
    for n in now.c:
        postorder(nodes[n])
    post[now.n] = ord
    ord += 1

n, q = map(int, input().split())

nodes = [0]
for i in range(1, n + 1):
    nodes.append(node(i)) 

for _ in range(n - 1):
    p, c = map(int, input().split())
    nodes[p].c.append(c)

ord = 1
pre = [0 for _ in range(n + 1)]
preorder(nodes[1])

ord = 1
post = [0 for _ in range(n + 1)]
postorder(nodes[1])

count = 0
for _ in range(q):
    u, v = map(int, input().split())

    if u == v:
        count += 1
    elif pre[u] < pre[v] and post[u] > post[v]:
        count += 1

print(count)

# 각 노드의 정보를 class로 nodes 리스트에 저장
# 노드 번호 순서대로 preorder와 postorder를 구한 뒤
# pre[u] < pre[v] and post[u] > post[v]이거나 u == v인 질의에 대해 True 카운트를 더함
# preorder, postorder 탐색과 각 노드의 저장, 질의에 대한 답이 모두 O(n)이므로
# 시간복잡도는 O(n)