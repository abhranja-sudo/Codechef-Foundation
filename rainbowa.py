t = int(input())
a = [1,2,3,4,5,6,7]
while t:
	t-=1
	n = int(input())
	arr = list(map(int,input().split()))
	start,end=0,n-1
	counter = 0
	flaglast = False
	flag = False
	if arr[start]==1 and arr[end]==1:
		while True:
			if counter==7 and (start == end or start+1 == end) :
					flag = True
			start+=1
			end-=1
			if end<start:
				break
			if arr[start]==a[counter] and arr[end]==a[counter]:
				pass
			if counter+1<7 and arr[start]==a[counter+1] and arr[end]==a[counter+1]:
				counter+=1
				
				pass
			
			pass

	if flag:
		print("yes")
	else:
		print("no")

