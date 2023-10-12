t = int(input())

for _ in range(t):
    nums = list(map(int, input().split()))

    nums.sort()

    ans = 'YES'
    minv = nums[0]
    count = 0
    for i in range(2, -1, -1):
        if nums[i] != minv:
            count += 1
        nums[i] -= minv
    
    for i in range(1, 3):
        if nums[i] != 0 and nums[i] != minv:
            if nums[i] % minv != 0:
                ans = 'NO'
            count += nums[i] / minv - 1

    if count > 3:
        ans = 'NO'
    
    print(ans)