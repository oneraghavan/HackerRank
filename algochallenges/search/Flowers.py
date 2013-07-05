import math
N, K = raw_input().split()
N = int(N)
K = int(K)
C = []

numbers = raw_input()

i = 0
for number in numbers.split():
   C.append( int(number) )
   i = i+1
C.sort(reverse=True)
totalcost = 0
for idx, val in enumerate(C):
    totalcost = totalcost + (math.floor(idx/K) + 1) * val

print int(totalcost)