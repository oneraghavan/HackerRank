#!/bin/python

# Head ends here
def insertionSort(ar):   
	v = ar[-1]
	for (i , e) in enumerate(ar[:-1][::-1]):
#		print e , v , i , len(ar)
		if v >= e :
			ar[len(ar)-i-1] = v
			print " ".join(map(str,ar))
			return
		else:
			ar[len(ar)-i-1] = e
			if i == len(ar) - 2:
				print " ".join(map(str,ar))
				ar[len(ar)-i-2] = v
		print " ".join(map(str,ar))
	return    
    
# Tail starts here

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)