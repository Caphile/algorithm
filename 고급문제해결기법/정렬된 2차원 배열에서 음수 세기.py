def BS(subNums):    # 이진탐색 O(logn)
    global count

    m = len(subNums) // 2
    if m == 0:
        if subNums[0] < 0:
            count += 1
        return

    if subNums[m] < 0:
        count += m
        BS(subNums[m : ])
    else:
        BS(subNums[ : m])

n = int(input())
count = 0
for i in range(n):
    nums = list(map(int, input().split()))
    BS(nums)

print(count)

# 오름차순으로 정렬되어 있음이 보장되었으므로
# 선택한 구간의 중앙값이 음수라면 중앙값 왼쪽 부분은 모두 음수임이 보장되고
# 선택한 구간의 중앙값이 양수라면 중앙값 오른쪽 부분은 모두 양수임이 보장됨
# BS 함수의 사용횟수마다 찾아야 하는 구간이 반토막 남
# 따라서 O(logn)의 시간복잡도에 수행됨