t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    apples = list(map(int, input().split()))
    trees = list(map(int, input().split()))
    
    pins = [0]  # pins[i + 1] - pins[i] : area
    for i in range(1, len(trees)):
        if trees[i - 1] % trees[i] != 0:
            pins.append(i)
    pins.append(n)

    ans = -1
    for i in range(len(pins) - 1):
        s = pins[i]
        e = pins[i + 1]

        total = 0
        l = s
        for r in range(s, e):
            total += apples[r]
            while total > k:
                total -= apples[l]
                l += 1
            ans = max(ans, r - l + 1)

    print(ans)
