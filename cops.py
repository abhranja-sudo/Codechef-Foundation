for t in range(int(input())):
	M,x,y = map(int,input())
	cop = list(map(int,input().split()))
	check = [0]*101
	for i in cop:
		min = i-x*y
		max = i+x*y
		for j in range(min,max+1):
			if(j>0 and j<=100):
				check[j] = 1

	count =0
	for i in range(1,101):
		if check[i]==1:
			count+=1
			pass
	print(count)