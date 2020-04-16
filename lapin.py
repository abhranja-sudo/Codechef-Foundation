for t in range(int(input())):
	s = str(input())
	size = len(s)
	a = [0]*130
	b = [0]*130
	if size%2==0:
		mid = size//2
		for i in range(0,mid):
			a[ord(s[i])]+=1

		for i in range(mid,size):
			b[ord(s[i])]+=1
	else:
		mid = size//2
		for i in range(0,mid):
			a[ord(s[i])]+=1

		for i in range(mid+1,size):
			b[ord(s[i])]+=1

	flag = True
	for i in range(130):
		if a[i]!=b[i]:
			flag = False
			pass
	if flag == True:
		print("YES")
	else:
		print("NO")
