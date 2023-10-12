t = int(input())

def conv(ori, trg):
    return abs(ord(ori) - ord(trg))

for _ in range(t):
    n = int(input())

    sqr = []
    for _ in range(n):
        sqr.append(list(input()))

    new_sqr = []
    for x in range(n - 1, -1, -1):
        line = ""
        for y in range(n - 1, -1, -1):
            line = sqr[y][x] + line
        new_sqr.append(line)

    sum = 0
    for y in range(n):
        for x in range(n):
            a, b = sqr[y][x], new_sqr[y][x]
            if a != b:
                sum += conv(a, b)
    
    print(sum / 2)