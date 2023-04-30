class makeSL:
    def __init__(self, target):
        self.n = len(target)
        self.target = target
        temp = sorted(target)
        self.idx = {temp[i] : i for i in range(self.n)}

        self.S = [0 for _ in range(self.n)]  
        self.L = [0 for _ in range(self.n)]

    def run(self):
        self.countSmall()
        self.countLarge()

    def countSmall(self):
        self.bit = [0] * (self.n + 1)
        for i in range(self.n):
            self.S[i] = self.preSum(self.idx[self.target[i]])
            self.update(self.idx[self.target[i]] + 1, 1)

    def countLarge(self):
        self.bit = [0] * (self.n + 1)
        for i in range(self.n - 1, -1, -1):
            self.L[i] = self.preSum(self.n) - self.preSum(self.idx[self.target[i]] + 1)
            self.update(self.idx[self.target[i]] + 1, 1)

    def update(self, i, val):
        while i < self.n + 1:
            self.bit[i] += val
            i += self.LSB(i)

    def preSum(self, i):
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= self.LSB(i)
        return s

    def LSB(self, i):
        return i & -i

n = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))

orderBy = sorted(enumerate(zip(P, Q)), key = lambda x : (x[1][0], x[0]))
t, newPQ = zip(*orderBy)
nP, nQ = zip(*newPQ)

SL = makeSL(list(nQ))
SL.run()

ans = 0
for i in range(n):
    ans += SL.S[i] * SL.L[i]
print(ans)

# P, Q를 묶어서 P에 대한 오름차순으로 정렬 O(nlogn)
# P는 서로 값이 다른 어떤 세 인덱스를 골라도 트리플이 성립하므로
# Q에서 트리플이 성립 가능한 개수를 세면 됨

# 세 인덱스중 중간에 있는 인덱스의 값이 다른 두 값 사이에 존재해야 하므로 S, L 리스트를 채움
# S[i] : nQ[0] ~ nQ[i - 1] 중 nQ[i]보다 작은 수의 개수
# L[i] : nQ[i + 1] ~ nQ[n] 중 nQ[i]보다 큰 수의 개수

# nQ[i]보다 작은 수 가 S[i]개, 큰 수가 L[i]개 이므로
# 0부터 n까지 모든 i에 대해 S[i] * L[i]을 합한 값이 답이 됨
# S, L은 BIT 자료구조를 통해 채움 O(nlong)
# 따라서 시간복잡도는 O(nlogn)

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