# coding = cp949

def func(s, e, c):
    if c > 3:
        return 4
    while s < e:
        if stn[s] == stn[e]:
            s += 1
            e -= 1
        else:
            return(min(func(s + 1, e, c + 1), func(s, e - 1, c + 1)))
    return c

stn = input()
n = len(stn)

res = func(0, n - 1, 0)
if res == 4:
    print(-1)
else:
    print(res)
    
# 함수가 재귀적으로 호출되며 팰린드롬 확인
# min(func(s + 1, e, c + 1), func(s, e - 1, c + 1)) 에서 2번을 깊이 k만큼 동작하므로 O(k^2)
# while문을 돌며 n길이 문자열을 탐색하므로 O(n)
# 단, k가 3으로 고정되어 있으므로 k^2는 8의 값을 가짐
# 결론적으로 O(k^2 n) = O(8 * n) = O(n)의 시간복잡도를 가짐