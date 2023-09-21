n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
d = [[[0] * (k + 1) for _ in range(n)] for _ in range(n)]

for j in range(n):
    for t in range(1, 4):
        if j + t > n:
            break
        d[0][j + t - 1][1] = max(d[0][j + t - 1][1], sum(grid[0][j:j + t]))

        
for i in range(1, n):
    for j in range(n):
        for t in range(1, 4):
            if j + t > n:
                break
            for x in range(1, k + 1):
                if d[i - 1][j][x] != 0:
                    d[i][j + t - 1][x] = max(d[i][j + t - 1][x], d[i - 1][j][x - 1] + sum(grid[i][j:j + t]))

answer = max(d[n - 1][j][k] for j in range(n))
if answer == 0:
    print(-1)
else:
    print(answer)