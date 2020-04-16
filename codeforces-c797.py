import sys
inp = sys.stdin.readlines()
leninp= len(inp[0])-1 

stack = [0]*leninp
countOfLetters = [0]*130
top = -1
for char in inp[0]:
	countOfLetters[ord(char)]+=1

i=0
result = ""
while i<leninp:
	if top!=-1:
		temp = stack[top]
		ordTemp = ord(temp)
		flag = False
		for j in range(ord('a'),ordTemp,1):
			if countOfLetters[j]>0:
				flag = True
				# print("yes ")
				break
		if flag==True:
			stack[top+1] = inp[0][i]
			top+=1
			countOfLetters[ord(stack[top])]-=1
			i+=1
		else:
			result= result+stack[top]
			top-=1
	else:
		stack[top+1] = inp[0][i]
		top+=1
		countOfLetters[ord(stack[top])]-=1
		i+=1


# print(stack)
while top!=-1:
	result = result+stack[top]
	top-=1
	pass

print(result)