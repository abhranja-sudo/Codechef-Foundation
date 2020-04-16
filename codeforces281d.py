import sys
inp = sys.stdin.readlines()
n = int(inp[0])
arr = list(map(int,inp[1].split()))
maxglobal = -1
top = -1
stack = [0]*n
for i in range(n):
	while top!=-1:
		print("stack top "+ str(stack[top])+ " element "+ str(arr[i]))
		maxglobal = max(maxglobal,stack[top]^arr[i])
		if stack[top]<arr[i]:
			top-=1
		else:
			break
	stack[top+1] = arr[i]
	top+=1 

print(maxglobal)
