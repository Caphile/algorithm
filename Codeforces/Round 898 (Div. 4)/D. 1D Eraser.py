t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    cells = input()

    count, i = 0, 0
    while (i < len(cells)): 
        if cells[i] == 'B':
            count += 1
            i += k - 1
        i += 1

    print(count)   