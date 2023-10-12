t = int(input())

ans = []
for _ in range(t):
    n, m = map(int, input().split())

    a = input()
    b = input()

    a *= m

    idx = a.find(b)
    if idx == -1:
        ans.append(-1)
    else:
        end = idx + m

        count = 0
        while end > n:
            count += 1
            n *= 2

        ans.append(count)

for i in ans:
    print(i)