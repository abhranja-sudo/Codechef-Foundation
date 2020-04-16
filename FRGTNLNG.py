t = int(input())
while t:
	t-=1
	n,k=map(int,input().split())
	stringList = list(map(str,input().split()))
	output = ["NO"]*n
	for x in range(k):    
		temp = list(map(str,input().split()))
		for i in range(1,int(temp[0])+1):
			if temp[i] in stringList:
				index = stringList.index(temp[i])
				output[index] = "YES"
		pass
	pass
	for i in output:
		print(i,end=" ")
	print()