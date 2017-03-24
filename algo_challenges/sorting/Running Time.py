def insertToplace(ar):
	v = ar[-1]
	for (i , e) in enumerate(ar[:-1][::-1]):
		if v >= e :
			ar[len(ar)-i-1] = v
			return ar ,len(ar) -1 - (len(ar)-i-1)
		else:
			ar[len(ar)-i-1] = e
			if i == len(ar) - 2:
				ar[len(ar)-i-2] = v
				return ar , len(ar) - 1
	return ar,0


def insertionSort(ar):
	count = 0
	for i in range(2,len(ar)+1):
		newChanged,shift = insertToplace(ar[:i])
		oldChanged = ar[:i]
		ar = newChanged + ar[i:]
		if not newChanged == oldChanged:
			count = count + shift
	sys.stdout.write(str(count) + '\n' )

import sys
dump = sys.stdin.readline()
arraystr = sys.stdin.readline()
ar = [int(i) for i in arraystr.split(' ')]
insertionSort(ar)