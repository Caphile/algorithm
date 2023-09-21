n = int(input())
for _ in range(n):
    m = int(input())
    digits = list(map(int, input().split()))
    digits[digits.index(min(digits))] += 1

    sum = 1
    for i in digits:
        sum *= i

    print(sum)