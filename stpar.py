import sys
inp = sys.stdin.readlines()
i = 0
while int(inp[i])!=0:
	i+=1
	arr = list(map(int,inp[i].split()))
	arrlen = len(arr)
	i+=1
	counter =1
	sta = [0]*arrlen
	top= -1
	j=0
	while(True):
		if(counter == arrlen+1 or j==arrlen):
			break
		if arr[j]==counter:
			counter+=1
			j+=1
		elif arr[j]!=counter:
			if top!=-1 and sta[top]==counter:
				counter+=1
				top-=1
			else:
				sta[top+1]= arr[j]
				top+=1
				j+=1
				pass
	while(True):
		if counter!=sta[top] or top==-1:
			break
		else:
			top-=1
			counter+=1
	# print(sta)
	# print(counter)
	if counter ==arrlen+1:
		print("yes")
	else:
		print("no")

	pass