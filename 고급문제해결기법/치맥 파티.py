a, b, t = map(int, input().split())

maxc = 0
mint = 10000
i = 0
while 1:
    temp = t - a * i
    if temp < 0:
        break
    count = temp // b + i   # 먹은 치킨 수
    time = temp % b         # 남은 시간

    if mint > time:
        mint = time
        maxc = count
    elif not time and maxc < count:
        maxc = count
    i += 1

if not mint:
    print(maxc)
else:
    print(maxc, mint)

# 모든 가능한 (후라이드 수, 양념 )에 대해 먹은 치킨의 수, 남은 시간을 비교
# 1. 이전에 저장된 시간보다 현재 시간이 줄었다면 시간과 먹은 수를 갱신
# 2. 남은 시간이 0이라면 먹은 수만 갱신
# 최대 t/a또는 t/b의 길이만큼만 반복하면 되므로 O(t/a) 혹은 O(t/b)이 가능함