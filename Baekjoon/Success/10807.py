n = int(input())
arr = list(map(int, input().split()))

find = int(input())
count = 0
for i in arr:
    if i == find:
        count += 1

print(count)