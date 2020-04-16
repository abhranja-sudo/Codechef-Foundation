t = int(input())
while t!=0:
	t-=1
	n=int(input())
	w=list(map(int,input().split()))
	count =0
	while True:
		minIndex = w.index(min(w))
		maxIndex = w.index(max(w))
		if w[minIndex] != w[maxIndex]:
			diff = w[maxIndex]-w[minIndex]
			w = [x+diff for x in w]
			w[maxIndex]-=diff
			count+=diff
		else:
			print(count)
			break
	
	pass