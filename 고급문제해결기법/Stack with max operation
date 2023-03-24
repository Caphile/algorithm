count = 0
stack = ['EMPTY']		# 스택
maxStack = ['EMPTY']	# maxStack[i] : i개의 정수가 있을때 그중 가장 큰 수
while(1):
	cmd = input().split()
	
	if cmd[0] == 'push':	# push
		v = int(cmd[1])	# push value
		stack.append(v)
		if not count or maxStack[count] < v:
			maxStack.append(v)
		else:
			maxStack.append(maxStack[count])
		count += 1

	elif cmd[0] == 'pop':	# pop
		if count:
			print(stack.pop())
			maxStack.pop()
			count -= 1
		else:
			print(stack[count])

	elif cmd[0] == 'max':	# max
		print(maxStack[count])

	else:					# exit
		break
