T = int(input())
for x in range(T):
	inpnc = list(map(int,input().split()))
	n = inpnc[0]
	c = inpnc[1]
	inpa = list(map(int,input().split()))
	sum =0
	for i in range(len(inpa)):
		sum+=inpa[i]
	if sum<c:
		print("No")
	else:
		print("Yes")

		# cook your dish here
t=int(input())
while(t!=0):
    t-=1
    n,c=map(int,input().split())
    a=list(map(int,input().split()))
    sum_a=sum(a)
    if c<sum_a:
        print("No")
    else:
        print("Yes")