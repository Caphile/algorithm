t = int(input())

for _ in range(t):
    n = int(input())

    sqr = []
    for _ in range(n):
        sqr.append(list(input()))

    ans = 0
    for i in range(n // 2):
        for j in range(n // 2):
            now = [sqr[j][i], sqr[i][n - 1 - j], sqr[n - 1 - i][j], sqr[n - 1 - j][n - 1 - i]]
            now = [ord(x) for x in now]

            now_max= max(now)
            ans += now_max * 4 - sum(now)
    
    print(ans)