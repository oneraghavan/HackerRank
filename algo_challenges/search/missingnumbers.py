N =  raw_input()
A =  raw_input().split()
T =  raw_input()
B =  raw_input().split()

A = map(int,A)
B = map(int,B)
A_missed = []
B_missed = []
i , j = 0 , 0
while(j != len(B) - 1 ):
	if len(A_missed) == 0:
		if A[i] != B[j]:
			A_missed.append(A[i])
			B_missed.append(B[j])
			i += 1
			j += 1
		else:
			i += 1
			j += 1
	else:
		if B[j] in A_missed:
			A_missed.remove(B[j])
			j += 1	
		elif A[i] == B[j]:
			i += 1
			j += 1
print " ".join(map(str,B_missed))