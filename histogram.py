import sys

# Python3 program to find maximum 
# rectangular area in linear time 

def max_area_histogram(histogram): 
	stack = [0]*100000
	top = -1
	max_area = 0
	index =0
	while index < len(histogram):

		if(top == -1 or histogram[index]>=histogram[stack[top]]):
			stack[top+1] = index
			top+=1
			index+=1
		else:
			temp= stack[top]
			
			if top-1==-1:
				area = histogram[temp]*index
			else:
				area = histogram[temp]*(index-stack[top])
			print("i " + str(index-stack[top]))
			top-=1
			if(area>max_area):
				max_area = area

	print("TOP BEFORE"+ str(top))
	while top != -1:
		print("top "+ str(top))
		temp= stack[top]
		
		if top-1==-1:
			area = histogram[temp]*index
		else:
			area = histogram[temp]*(index-stack[top])
		print("j "+str(index-stack[top]))
		top-=1
		if(area>max_area):
			max_area = area
		
	
	return max_area 

inp = sys.stdin.readlines()
i = 0
while(True):
	arr = list(map(int,inp[i].split()))
	i+=1
	if(arr[0]==0):
		break
	else:
		arr = arr[1:]
		print(max_area_histogram(arr))
