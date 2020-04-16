t = int(input())
while t:
	t-=1
	n,k=map(int,input().split())
	arr = list(map(int,input().split()))
	len = n-1
	count =0

	while len>=0:
		temp = arr[len]+k
		if temp%7==0:
			count+=1
			pass
		len-=1
		pass
	print(count)
	pass