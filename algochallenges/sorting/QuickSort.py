#!/bin/python

# Head ends here
def quickSort(ar):
	p = ar[0]
	resultLeft = []
	resultRight = []
	for num in ar[1:]:
		if num >=p :
			resultRight.append(num)
		else:
			resultLeft.append(num)

	if len(resultLeft) > 1:
		resultLeft = quickSort(resultLeft)
	if len(resultRight) > 1:
		resultRight = quickSort(resultRight)
	resultLeft.append(p)
	ar = resultLeft + resultRight
	print " ".join(map(str,ar))
	return ar

# Tail starts here

m = input()
ar = [int(i) for i in raw_input().strip().split()]
quickSort(ar)