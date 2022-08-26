n, k = map(int, input().split())
coin = []

for _ in range(n):
    c = int(input())
    coin.append(c)

sum = 0
for i in reversed(coin):
    temp = k // i
    if temp >= 1:
        k -= temp * i
        sum += temp

print(sum)