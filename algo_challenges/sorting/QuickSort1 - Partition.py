#!/bin/python

# Head ends here
def partition(ar):
	p = ar[0]
	resultLeft = []
	resultRight = [p]
	for num in ar[1:]:
		if num >=p :
			resultRight.append(num)
		else:
			resultLeft.append(num)
	result = resultLeft + resultRight
	print " ".join(map(str,result))

# Tail starts here

m = input()
ar = [int(i) for i in raw_input().strip().split()]
partition(ar)