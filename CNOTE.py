T = int(input())
while T>0:
	T-=1
	X,Y,K,N = map(int,input().split())
	P = []
	C = []
	for i in range(N):
		p,c = map(int,input().split())
		P.append(p)
		C.append(c)

	i=0
	pages_req = X-Y
	flag = False
	while i!=len(P):
		if P[i]>=pages_req and C[i]<=K:
			flag = True
			break
		i+=1
	if flag== True:
		print("LuckyChef")
	else:
		print("UnluckyChef")
