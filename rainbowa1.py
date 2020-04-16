l=[1,2,3,4,5,6,7]
for x in range(int(input())):
    a=int(input())
    b=list(map(int,input().split()))
    c=0
    for y in b:
        if y not in l:
            c=1
            break
    if c==0 and b==b[::-1] and len(set(b))==7:
        print('yes')
    else:
        print('no')