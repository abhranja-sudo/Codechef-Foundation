import sys
inp = sys.stdin.readlines()
i = 1
t = int(inp[0]) 
while t!=0:
	t-=1
	inp1 = inp[i]
	leninp1 = len(inp1)-1
	# print("leninp1 "+ str(leninp1))
	i+=1
	stack = [0]*len(inp1)
	top = -1
	# flag = False
	counter =0
	for j in range(leninp1):
		if top==-1 and inp1[j]==">":
			counter = j
			flag = True
			break
		elif inp1[j]=="<":
			top+=1
		elif inp1[j] == ">":
				top-=1
				if top==-1:
					counter = j+1
					pass

	print(counter)
	