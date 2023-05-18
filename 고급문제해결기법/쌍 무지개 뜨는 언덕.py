def calc(opt):
    global n, k
    global nowCount, numCount
    global s, e

    if opt == 's':
        nows[line[s]] -= 1
        if nows[line[s]] == 0:
            nowCount -= 1
        nums[line[s]] += 1
        if nums[line[s]] == 1:
            numCount += 1
        s += 1
    else:
        e += 1
        nows[line[e]] += 1
        if nows[line[e]] == 1:
            nowCount += 1
        nums[line[e]] -= 1
        if nums[line[e]] == 0:
            numCount -= 1

n, k = map(int, input().split())

nows = [0 for _ in range(k + 1)]    # 현재 구간에서 포함하는 점의 각 수
nums = [0 for _ in range(k + 1)]    # 현재 구간을 제외한 모든 점의 각 수
nowCount = 0    # 0이 아닌 nows의 개수
numCount = k    # 0이 아닌 nums의 개수

line = []
for i in range(n):
    c = int(input())
    nums[c] += 1
    line.append(c)
line += line

s, e = 0, 0
target = line[0]
seq = False
rainbows = []
while s < n and e < 2 * n:  # 한 바퀴를 다 돌때까지
    if e - s + 1 > n:
        calc('s')
        continue
    if not nows[target]:
        seq = False
        calc('e')
    else:
        if nowCount == k:   # 무지개   
            if numCount == k:   # 쌍무지개
                if seq:
                    rainbows.pop()
                rainbows.append(e - s + 1)
                seq = True
            calc('s')
        else:
            seq = False
            calc('e')

if rainbows == []:
    print(0)
else:
    print(min(rainbows))
