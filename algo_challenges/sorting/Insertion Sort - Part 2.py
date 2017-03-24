#!/bin/python

# Head ends here
def insertToplace(ar):
#	print "Start" , ar
	v = ar[-1]
	for (i , e) in enumerate(ar[:-1][::-1]):
#		print e , v , i , len(ar)
		if v >= e :
			ar[len(ar)-i-1] = v
#			print "changed"," ".join(map(str,ar))
			return ar
		else:
			ar[len(ar)-i-1] = e
			if i == len(ar) - 2:
#				print " ".join(map(str,ar))
				ar[len(ar)-i-2] = v
#		print " ".join(map(str,ar))
	return ar


def insertionSort(ar):
#	print ar[:3] , ar[3:]
	for i in range(2,len(ar)+1):
#		print ar[i]
#		print ar[:i] , "============" ,insertToplace(ar[:i])
		newChanged = insertToplace(ar[:i])
		oldChanged = ar[:i]
		ar = insertToplace(ar[:i]) + ar[i:]
#		if not newChanged == oldChanged:
		print " ".join(map(str,ar))
#		print ar[:i] ,ar

# Tail starts here

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)