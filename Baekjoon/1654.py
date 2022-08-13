k, n = map(int, input().split())

s = 1
e = -1
lines = []
for i in range(k):
    lines.append(int(input()))
    if e == -1 or e < lines[i]:
        e = lines[i] + 1

while s < e:
    m = (s + e) // 2
    if s == m or e == m:
        break

    total = 0
    for i in lines:
        total += i // m

    if total >= n:
        s = m
    else:
        e = m

print(m)