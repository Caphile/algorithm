n = int(input())
for _ in range(n):
    now = input()
    score = 0
    if now[0] == 'a':
        score += 1
    elif now[1] == 'b':
        score += 1
    elif now[2] == 'c':
        score += 1

    if score == 0:
        print('NO')
    else:
        print('YES')