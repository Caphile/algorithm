def BS(s, e, x):    # 이진탐색 O(logn), 리스트 nums의 x번째 행의 구간[s, e]에서 탐색
    global is_found, k
    if not is_found:
        if s == e:
            if nums[x][s] == k:
                is_found = True
                print(x, s)
        else:
            m = (s + e) // 2        # 오름차순 정렬이므로
            if nums[x][m] >= k:     # k값이 nums[x][m]보다 크다면 다음 탐색 구간은 nums[x][s]부터 nums[x][m]
                BS(s, m, x)
            elif nums[x][m] < k:    # k값이 nums[x][m]보다 작다면 다음 탐색 구간은 nums[x][m + 1]부터 nums[x][e]
                BS(m + 1, e, x)

n, k = map(int, input().split())
nums = []
for i in range(n):
    nums.append(list(map(int, input().split())))

is_found = False    # 초기값
for i in range(len(nums)):  # 이진탐색 O(n)회 반복 = O(nlogn)
    BS(0, n - 1, i)

if not is_found:
    print(-1)

# 행 단위로 이진탐색 실시
# BS 함수의 사용횟수마다 찾아야 하는 구간이 반토막 남
# k값을 찾은 경우에는 다음 탐색구간을 [s, m]으로 두어 출력 우선순위가 더 높은 k의 위치를 탐색
# 이때 구간의 길이가 1이면서 처음으로 발견한 k의 위치가 정답
# 이진탐색을 n번 반복하므로 O(nlogn)의 시간복잡도에 수행됨