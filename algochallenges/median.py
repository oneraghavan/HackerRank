from math import floor
s = ['r','a','a','a','r','r','r']
X=  [1,1,2,1,1,2,1]
array1 = []
array2 = []

def median_of():
    if len(array)%2 == 0:
#        print 'even length'
        idxs = len(array)/2
#        print 'index',idxs , array[idxs] , array[idxs-1] , len(array)
        return float(array[idxs] + array[idxs-1]) / 2
    else:
#        print 'odd length'
        return array[int(floor(len(array)/2))]

for idx, op in enumerate(s):
    if op=='r':
        if len(array1) == 0 and len(array2) == 0:
            print 'Wrong!'
        else:
            if X[idx] in array1:
                array1.remove(X[idx])
            else:
                array1.remove(X[idx])
            print median_of()
    else:
        array.append(X[idx])
        array.sort()
        print median_of()


