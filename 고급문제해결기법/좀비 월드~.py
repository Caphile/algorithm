# coding = cp949

def findEvent(bef, now):
    if not bef or bef > now:
        return now
    return bef

n, l, k = map(int, input().split())
L, R = -1, 1
zombies = []    # 아이디, 현재위치, 진행방향
for i in range(n):
    loc, iden = map(int, input().split())
    zombies.append([iden, loc, int(iden / abs(iden))])

zombies = sorted(zombies, key = lambda x : x[1])    # 각 좀비를 위치를 기준으로 정렬, O(nlogn)

outList = []
while len(outList) < k:
    time = None
    newN = len(zombies)
    for i in range(newN - 1):
        nowZ = zombies[i]
        nextZ = zombies[i + 1]

        if not i and nowZ[2] == L:              # 추락(왼쪽)
            time = findEvent(time, nowZ[1])
        elif nowZ[2] == R and nextZ[2] == L:    # 충돌
            if nextZ[1] != nowZ[1]:
                time = findEvent(time, (nextZ[1] - nowZ[1]) / 2)
            else:
                zombies[i][2] *= -1
                zombies[i + 1][2] *= -1

    nowZ = zombies[newN - 1]
    if nowZ[2] == R:                            # 추락(오른쪽)
        time = findEvent(time, l - nowZ[1])

    subOut = []
    newZombies = []
    befZ = None
    for i in range(newN):
        nowZ = zombies[i]
        newLoc = nowZ[1] + time * nowZ[2]
        nowZombie = [nowZ[0], newLoc, nowZ[2]]

        if newLoc == 0 or newLoc == l:
            subOut.append(nowZ[0])
            continue
        
        newZombies.append(nowZombie)

        if i != newN - 1:
            if befZ and newLoc == befNewLoc:
                newZombies[i][2] *= -1
                newZombies[i - 1][2] *= -1

            befZ = nowZ
            befNewLoc = newLoc

    for i in sorted(subOut):
        outList.append(i)
    zombies = newZombies

print(outList[k - 1])

# 충돌 또는 추락을 하나의 이벤트로 보고
# 가장 빠르게 발생할 이벤트 시간을 기준으로 시뮬레이션을 돌림
# 좀비를 위치 기준으로 정렬하는데 O(nlogn)
# while을 돌면서 최악의 경우 O(n^2)
# 시간복잡도는 O(n^2)