n, b, a = map(int, input().split())
prices = list(map(int, input().split()))

prices.sort()   # O(nlogn)

subSum = [prices[0]]    # 부분합
for c, i in enumerate(prices[1 : ]):
    subSum.append(subSum[c] + i)

for i in range(n):  # O(n)
    if i < a:   # 할인 가능 개수가 선택한 총 개수보다 많거나 같은 경우
        if b < subSum[i] / 2:
            ans = i
            break
    else:       # 할인 가능 개수보다 더 많이 선택한 경우
        if b < (subSum[i] + subSum[i - a]) / 2:
            ans = i
            break
    ans = i + 1

print(ans)

# 오름차순으로 정렬을 하고
# 가격이 낮은 순으로 i개를 선택한다.
# i번째 부터 i-a번째 선물은 반값만 적용한다.
# O(nlogn) 정렬 후 O(n) 탐색을 진행하므로 O(nlogn) 시간복잡도를 가진다.