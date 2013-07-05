import sys
diffarray = sys.stdin.readline()
arraystr = sys.stdin.readline()
diff = [int(i) for i in diffarray.split(' ')][1]
array = [int(i) for i in arraystr.split(' ')]
array.sort()
count = 0
arrayRev = array[:-1][::-1]

for (i , e) in enumerate(array[1:]):
    for num in arrayRev[(len(arrayRev) - 1) - i:]:
        if abs(e - num ) == diff:
            count = count + 1
            break
        elif abs(e - num ) > diff:
            break

print count
