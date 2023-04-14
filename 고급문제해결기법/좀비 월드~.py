# coding = cp949
'''
# 소수인 loc이 발생해 폐기
n, l, k = map(int, input().split())
L, R = -1, 1
left, right = [], []
for _ in range(n):
    loc, iden = map(int, input().split())
    if iden > 0:    # 우측
        right.append([loc, iden])
    else:           # 좌측
        left.append([loc, iden])

outList = []    # 밖으로 떨어진 좀비
while len(outList) < k:  
    road = [None for _ in range(l + 1)]     # 아이디, 위치, 방향
    check = [None for _ in range(l + 1)]

    for idx in range(len(right)):
        zombie = right[idx]
        road[zombie[0]] = [zombie[1], zombie[0], R]
    for idx in range(len(left)):
        zombie = left[idx]
        road[zombie[0]] = [zombie[1], zombie[0], L]

    before = None
    coliLoc = None
    triggerTime = 100000    # 현재 이후 최초 이벤트 발생까지 남은 시간
    zombies = []
    for loc in range(len(road)):
        now = road[loc]
        if now:
            zombies.append(now)
            if not before and now[2] == L:          # 추락
                triggerTime = min(triggerTime, now[1])
            elif now[2] == L and before[2] == R:    # 충돌
                triggerTime = min(triggerTime, (now[1] - before[1]) / 2)
                if triggerTime == (now[1] - before[1]) / 2:
                    coliLoc = now[1] + now[2] * triggerTime
            before = now
            
    if before[2] == R:
        triggerTime = min(triggerTime, l - before[1])

    left, right = [], []
    thisOut = []
    for z in zombies:
        newLoc = z[1] + z[2] * triggerTime

        if newLoc == 0 or newLoc == l:  # 추락
            thisOut.append(z[0])
        elif coliLoc and coliLoc == newLoc:
            if z[2] == R:
                left.append([newLoc, z[0]])
            else:
                right.append([newLoc, z[0]])
        elif z[2] == R:
            right.append([newLoc, z[0]])
        else:
            left.append([newLoc, z[0]])

    for i in sorted(thisOut):
        outList.append(i)

print(outList)
'''

'''
# 소수인 newLoc이 발생해 폐기
n, l, k = map(int, input().split())
L, R = -1, 1
left, right = [None for _ in range(l + 1)], [None for _ in range(l + 1)]
for _ in range(n):
    loc, iden = map(int, input().split())
    if iden > 0:   # 우측
        right[loc] = iden
    else:           # 좌측
        left[loc] = iden

outList = []    # 밖으로 떨어진 좀비
while len(outList) < k:
    road = []   # 아이디, 위치, 방향
    check = []
    for loc in range(l + 1):
        if left[loc]:
            road.append([left[loc], loc, L])
            left[loc] = None
        if right[loc]:
            road.append([right[loc], loc, R])
            right[loc] = None
        check.append(False)

    triggerTime = 100000    # 현재 이후 최초 이벤트 발생까지 남은 시간
    for idx in range(len(road)):
        if road[idx][2] == R:
            if idx == len(road) - 1:
                triggerTime = min(triggerTime, l - road[idx][1])
            elif road[idx + 1][2] == L:
                triggerTime = min(triggerTime, (road[idx + 1][1] - road[idx][1]) / 2)

        if road[idx][2] == L and idx == 0:
            triggerTime = min(triggerTime, road[idx][1])

    thisOut = []
    for idx in range(len(road)):
        newLoc = road[idx][1] + road[idx][2] * triggerTime
        if not check[newLoc]:
            if newLoc == 0 or newLoc == l:
                thisOut.append(road[idx][0])
            elif road[idx][2] == R:
                right[newLoc] = road[idx][0]
            else:
                left[newLoc] = road[idx][0]
            check[newLoc] = True
        else:
            if road[idx][2] == R:
                temp = left[newLoc]
                left[newLoc] = road[idx][0]
                right[newLoc] = temp
            else:
                temp = right[newLoc]
                right[newLoc] = road[idx][0]
                left[newLoc] = temp

    for i in sorted(thisOut):
        outList.append(i)

print(outList[k - 1])
'''