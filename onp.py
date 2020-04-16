import sys
inp = sys.stdin.readlines()
inpin =1
for _ in range(int(inp[0])):
	expression = inp[inpin]
	inpin+=1
	lenexp = len(expression)
	stalett = [0]*lenexp
	toplett = -1
	staoper = [0]*lenexp
	topoper = -1
	exprange = ["+","-","*","/","^"]
	for i in range(lenexp):
		if expression[i] in exprange:
			staoper[topoper+1] = expression[i]
			topoper+=1
		elif expression[i] == ")":
			strtemp = ""
			for j in range(toplett,-1,-1):
				if stalett[j]=="(":
					toplett-=1
					strtemp+=staoper[topoper]
					topoper-=1
					stalett[toplett+1] = strtemp
					toplett+=1
					break
					pass
				else:
					strtemp= stalett[j]+strtemp
					toplett-=1
		else:
			stalett[toplett+1] = expression[i]
			toplett+=1

	print(stalett[0])