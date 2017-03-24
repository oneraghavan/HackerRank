N = int(raw_input())

s = []
X = []

for i in range(0, N):

   tmp = raw_input()
   a, b = [xx for xx in tmp.split(' ')]
   s.append(a)
   X.append(int(b))

from math import floor
array = []
def median_of():
    if len(array)%2 == 0:
        idxs = len(array)/2
        return float(array[idxs] + array[idxs-1]) / 2
    else:
        return array[int(floor(len(array)/2))]

for idx, op in enumerate(s):
    if op=='r':
        if len(array) == 0:
            print 'Wrong!'
        else:
            array.remove(X[idx])
            if len(array) == 0:
                print 'Wrong!'
            else:
                print median_of()
    else:
        array.append(X[idx])
        array.sort()
        print median_of()

