totalCost = int(input())
totalNum = int(input())

sum = 0
for i in range(totalNum):
    cost, num = map(int, input().split())
    sum += cost * num

if sum == totalCost:
    print("Yes")
else:
    print("No")