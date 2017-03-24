import math
import sys
inputtext = raw_input()
inputtext = list(inputtext)
row_count , col_count = int(math.floor(math.sqrt(len(inputtext)))) , int(math.ceil(math.sqrt(len(inputtext)))) 
for i in range(col_count):
	sys.stdout.write("".join(inputtext[i::col_count]) + " ")
