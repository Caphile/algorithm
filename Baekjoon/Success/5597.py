num_list = [1 for _ in range(31)]
num_list[0] = [0]

for _ in range(28):
    n = int(input())
    
    if num_list[n] == 1:
        num_list[n] = 0

for c, i in enumerate(num_list):
    if i == 1:
        print(c)