import sys
inp = sys.stdin.readlines()
i = 1
for t in range(int(inp[0])):
	n = int(inp[i])
	i+=1
	arr = list(map(int,inp[i].split()))
	i+=1
	change = -1
	for i in range(n-1,-1,-1):
		if(i-1>=0):
			#print(i-1)
			if(arr[i-1]<arr[i]):
				temp = arr[i-1]
				arr[i-1] = arr[i]
				arr[i] = temp
				change = i-1
				break
	if(change == -1):
		print(-1)
	else:
		arr1 = arr[change+1:n]
		arr1.sort()
		#arr = arr[change+1:n].sort()
		arr[change+1:n] = arr1
		st = ""
		for i in arr:
			st+=str(i)
		print(int(st))