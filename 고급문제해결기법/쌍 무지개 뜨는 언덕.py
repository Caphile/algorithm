def move(opt):
    global n
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
    elif opt == 'e':
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

s, e = 0, -1
move('e')
seq = False
rainbows = []
while s < n:  # 한 바퀴를 다 돌때까지
    if nowCount == k:       # 무지개   
        if numCount == k:   # 쌍무지개
            if seq:
                rainbows.pop()
            rainbows.append(e - s + 1)
            seq = True
        move('s')
    else:
        if e + 1 == n:
            break
        seq = False
        move('e')

if not len(rainbows):
    print(0)
else:
    print(min(rainbows))

# 구간을 s부터 e까지라고 했을때 이 구간이 무지개가 만들어지는지 확인
# 무지개가 만들어지는 경우는 nowCount가 k값과 같을때,
# 쌍무지개가 만들어지는 경우는 무지개가 만들어지는 상태에서 numCount가 k값과 같을때
# 1. 무지개가 만들어진다면
# 1-1. 쌍무지개가 만들어진다면 무지개 길이 저장 후 s + 1
# 이때 s + 1를 해서 똑같이 쌍무지개가 생길 수 있으므로 seq 상태 가져감
# 1-2. 쌍무지개를 만들지 못한다면 s + 1
# 2. 무지개가 만들어지지 않는다면 e + 1
# 저장된 쌍무지개가 있다면 그 중 최소값, 없다면 0을 출력
# s와 e가 최대 n번까지만 탐색하므로 (move함수도 O(1))
# O(n) 시간복잡도를 가짐