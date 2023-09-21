def calc(p_idx, v_idx):
    return abs(price[p_idx] - value[v_idx])

def minmin(A, B):
    if A[0] < B[0]:
        tp, tg = A
    elif A[0] > B[0]:
        tp, tg = B
    else:
        tp, tg = A[0], min(A[1], B[1])
    return (tp, tg)

n = int(input())
value = map(int, input().split())
price = map(int, input().split())

value = sorted(value)
price = sorted(price)

d = [[float('inf') for _ in range(4)] for _ in range(n)]
gift = [[float('inf') for _ in range(4)] for _ in range(n)]

d[0][0] = calc(0, 0)
d[1][0] = d[0][0] + calc(1, 1)
d[1][2] = calc(1, 0)
d[1][3] = calc(0, 1)
gift[1][3] = value[0]
for i in range(2, n):
    # d[i][0]
    d[i][0] = d[i - 1][0] + calc(i, i)

    # d[i][1]
    A = (d[i - 1][1], gift[i - 1][1])
    B = (d[i - 1][2], value[i - 1])
    C = (d[i - 1][3], gift[i - 1][3])
    tp, tg = minmin(minmin(A, B), C)

    d[i][1] = tp + calc(i, i)
    gift[i][1] = tg

    # d[i][2]
    A = d[i - 2][0]
    B = d[i - 1][2]
    tp = min(A, B)

    d[i][2] = tp + calc(i, i - 1)

    # d[i][3]
    A = (d[i - 2][0], value[i - 1])
    B = (d[i - 1][3], gift[i - 1][3])
    tp, tg = minmin(A, B)

    d[i][3] = tp + calc(i - 1, i)
    gift[i][3] = tg

if gift[n - 1][1] == float('inf'):
    gift[n - 1][1] = value[n - 1]
gift[n - 1][2] = value[n - 1]

minSum = float('inf')
for i in range(n):
    nowSum = d[n - 1][0] - calc(i, i)
    if minSum >= nowSum:
        if minSum == nowSum:
            tg = min(value[i], tg)
        else:
            minSum = nowSum
            tg = value[i]

resSum = [minSum] + d[n - 1][1 : ]
resTg = [tg] + gift[n - 1][1 : ]

minSum = float('inf')
for i in range(4):
    if minSum >= resSum[i]:
        if minSum == resSum[i]:
            ans = min(ans, resTg[i])
        else:
            minSum = resSum[i]
            ans = resTg[i]

print(ans)


# 현재 순혈 |     d[i][0], + diff(pri[i] - val[i])
#   이전 |            d[i - 1][0], 미정

# 현재 잡종 |     d[i][1], + diff(pri[i] - val[i])
#   이전 |            d[i - 1][1]
#   이전 /            d[i - 1][2], gift : val[i - 1]
#   이전 \            d[i - 1][3]

# 현재 /          d[i][2], + diff(pri[i] - val[i - 1])
#   이전 |            d[i - 2][0], 미정
#   이전 /            d[i - 1][2], 미정

# 현재 \          d[i][3], + diff(pri[i - 1] - val[i])
#   이전 |            d[i - 2][0], gift : val[i - 1]
#   이전 \            d[i - 1][3]