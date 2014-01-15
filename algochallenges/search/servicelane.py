import math
N , T = raw_input().split()
T = int(T)

widths = raw_input().split()
widths = [int(x) for x in widths] 

for i in range(T):
	entry , exit = raw_input().split()
	entry = int(entry)
	exit = int(exit)
	print min(widths[entry:exit+1])
	
