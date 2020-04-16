import sys
inp = sys.stdin.readlines()
inp1 = inp[0]
leninp1 = len(inp1)
stack = [0]*leninp1
top = -1
stack1 = [0]*leninp1
top1 = -1
maxCount = 0
count = 0
repetetion = [0]*leninp1
for i in range(leninp1):
	if inp1[i]==')' and stack[top]=='(':
		top-=1
		
		count = i-stack1[top1]+1
		repetetion[count]+=1
		top1-=1
		# print(count)
		maxCount = max(maxCount,count)
		
	elif inp1[i]=='(':
		stack[top+1] = '('
		top+=1
		stack1[top1+1] = i
		top1+=1
	else:
		stack[top+1] = ')'
		top+=1
		stack1[top1+1] = i
		top1+=1
if maxCount!=0:
	print(str(maxCount)+" "+str(repetetion[maxCount]))
else:
	print("0 1")
	