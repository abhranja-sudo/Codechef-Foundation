for t in range(int(input())):
	n = int(input())
	s = str(input())
	count = 0
	for i in s:
		if i == "1":
			count+=1
	if(count != 0 and count != 1 and count != 2):
		fact = 1
		for i in range(1,count+1):
			fact *= i 

		factdeno = fact/count
		factdeno = factdeno/(count-1)

		combination = fact/(factdeno*2)
		totalCombination = combination + count
		print(int(totalCombination))
	if count ==0:
		print(0)
	if count ==1:
		print(1)
	if (count ==2):
	    print(2)
		
