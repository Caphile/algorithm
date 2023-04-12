n, k = map(int, input().split())
nums = list(map(int, input().split()))

subsum = [0]	# 부분합
for c, i in enumerate(nums):	# O(n)
	subsum.append(subsum[c] + i)
	
isTrue = False
s, e = 0, 1
while e < n:	# O(n)
	nowSum = subsum[e] - subsum[s]	# nowSum = nums[s]부터 nums[e]까지 더한 값
	
	if not nowSum or nowSum < k:
		e += 1
	elif nowSum > k:
		s += 1
	elif nowSum == k:
		isTrue = True
		break
		
print(isTrue)

# 부분합을 구해서 리스트에 저장한 후에 O(n) s, e 두 포인트를 주고 반복문을 돌면서 O(n)
# nowSum이 k와 같다면 True를 리턴
# nowSum이 k보다 작다면 e에 1을 더함
# nowSum이 k보다 크다면 s에 1을 더함
# 만약 도중 s가 e보다 커지거나 같아진다면 e에 1을 더함
# True가 되는 값을 찾지 못했다면 e이 n과 같아질때까지 반복
# O(n) + O(n) = O(n)