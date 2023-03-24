count = 0
inStack = ['EMPTY']		# 입력을 받는 Stack
outStack = ['EMPTY']	# 출력을 내보내는 Stack
while(1):
	cmd = input().split()
	
	if cmd[0] == 'enq':	# enq
		v = int(cmd[1])	# push value
		inStack.append(v)
		count += 1

	elif cmd[0] == 'deq':	# deq
		if count:
			for _ in range(1, count):
				outStack.append(inStack.pop())
			print(inStack.pop())
			count -= 1

			for _ in range(count):
				inStack.append(outStack.pop())
		else:
			print(outStack[count])

	else:					# exit
		break
