t = int(input())
while t!=0:
	t-=1
	n=int(input())
	w=list(map(int,input().split()))
	count =0
	while True:
		flag = False
		maxIndex=0
		maxValue=w[0]
		for x in range(1,len(w)):
			if w[x]>maxValue:
				maxIndex = x
				maxValue = w[x]
				flag = True
				pass
			pass
		pass

		if flag==True:
			w = [x+1 for x in w]
			w[maxIndex]-=1
			count+=1
			pass
		else:
			print(count)
			break
	pass