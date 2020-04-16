import sys
inp = sys.stdin.readlines()
i=0
index = 0
while inp[i][0]!='-':
	braces = inp[i]
	lenin = len(inp[i])
	i+=1
	# print(lenin)
	# print(braces)
	stack = [0]*lenin
	top = -1
	count =0
	for j in range(lenin):
		# print("kl " + str(braces[j]))
		if braces[j]=='{':
			stack[top+1] = 0
			top+=1
			# print("a")
		elif braces[j] =='}':
			if(top!=-1 and stack[top]==0):
				top-=1
			elif top==-1:
				count+=1
				stack[top+1] =0
				top+=1
	if top!=-1:
		# print("top "+str(top))
		print(str(index+1)+". "+str(count+((top+1)//2))) 
	else:
		print(str(index+1)+ ". "+str(count))
	index+=1
	
