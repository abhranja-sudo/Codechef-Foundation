import sys

def max_area_histogram(histogram): 
	
	stack = list() 

	max_area = 0 # Initialize max area 

	# Run through all bars of 
	# given histogram 
	index = 0
	while index < len(histogram):

		if (not stack) or (histogram[stack[-1]] <= histogram[index]): 
			stack.append(index) 
			index += 1

		else: 
			# pop the top 
			top_of_stack = stack.pop() 

			temp = -1
			if stack:
				temp = index-stack[-1]-1
			else:
				temp = index
			# print("temp" + str(temp))

		# area = (histogram[top_of_stack] *
		# 	((index - stack[-1] - 1) 
		# 		if stack else index)) 
			area = histogram[top_of_stack]*temp
			# update max area, if needed 
			max_area = max(max_area, area) 
			# print(str(index) +"  "+ str(area))

	while stack: 
		
		# pop the top 
		top_of_stack = stack.pop() 
		temp = -1
		if stack:
			temp = index-stack[-1]-1
		else:
			temp = index
		# print("temp" + str(temp))

		# area = (histogram[top_of_stack] *
		# 	((index - stack[-1] - 1) 
		# 		if stack else index)) 
		area = histogram[top_of_stack]*temp
		# print(area)
		# update max area, if needed 
		max_area = max(max_area, area) 

	# Return maximum area under 
	# the given histogram 
	# print(stack)
	
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
