n = int(input())
for _ in range(n):
    score = 0
    for x in range(10):
        line = input()
        for y in range(10):
            if line[y] == 'X':
                for k in range(5):
                    if (x == k or x == 9 - k) or (y == k or y == 9 - k):
                        score += k + 1
                        break
    print(score)