t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    cols = list(map(int, input().split()))

    total = 0
    ans, prev_h = -1, -1
    for idx, c in enumerate(sorted(cols)):
        if prev_h != -1 and prev_h != c:
            temp = idx * (c - prev_h)
            if total + temp >= x:
                ans = prev_h + (x - total) // idx
                break
            total += temp
        prev_h = c        

    if ans == -1:
        ans = prev_h + (x - total) // n

    print(ans)