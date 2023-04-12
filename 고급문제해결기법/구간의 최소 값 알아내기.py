from heapq import heappush
from heapq import heappop

n, k = map(int, input().split())
nums = list(map(int, input().split()))

minHeap = []

for i in range(n):  # n번 반복 O(n)
    heappush(minHeap, (nums[i], i)) # heap 연산을 위해 O(logn)
    if i >= k - 1:
        while len(minHeap):
            minIdx = minHeap[0][1]
            if minIdx >= i - k + 1:
                break
            heappop(minHeap)

        print(minHeap[0][0], end = ' ')

# 모든 숫자들을 탐색하며 최소힙에 값과 인덱스를 추가 O(n * logn)
# i 값이 k - 1 이상인 시점부터 최소힙의 0번째 값을 불러옮. (i가 k - 1 이상이어야만 길이가 k인 구간이 만들어짐)
# 최소힙의 0번째 값을 불러올때 해당 값의 인덱스가 현재 구간에 속하는지 확인하고 속하지 않는다면 pop
# 이때 반복문을 사용하지만 결과적으로 힙에 n번 삽입, n번 삭제 연산을 하는 것이니 시간복잡도는 달라지지 않음
# i 가 k - 1 이상일 때만 힙의 0번째 값을 출력
# 시간복잡도는 O(nlogn)