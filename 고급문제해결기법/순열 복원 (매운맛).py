class recover:
    def __init__(self, n):
        self.n = n
        self.check = [0 for _ in range(n)]
        self.bit = [0 for _ in range(n + 1)]
        
    def run(self):
        self.prefixSum = []
        for i in range(self.n):
            self.prefixSum.append(self.preSum(i))
            self.update(i, self.check[i])

    def update(self, i, val):
        i += 1
        while i < self.n + 1:
            self.bit[i] += val
            i += self.LSB(i)

    def preSum(self, i):
        i += 1
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= self.LSB(i)
        return s

    def LSB(self, i):
        return i & -i

B = list(map(int, input().split()))
n = len(B)
A = [-1 for _ in range(n)]

rc = recover(n)
rc.run()

for i in range(n - 1, -1, -1):
    rc.check[i] = 1
    rc.run()