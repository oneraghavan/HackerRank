def getNumofmaxsq(x,y):
    if y%x == 0:
        return (x*y)/(x*x)
    for side in range(x,1,-1):
        print side
        if y%side == 0 and x%side == 0:
            return (x*y)/(side*side)

    return (x*y)

#K = int(raw_input())
#
#for i in range(0,k):
#    X,Y = raw_input().split()
#    X,Y = int(X),int(Y)
#    if X < Y :
#        print getNumofmaxsq(X, Y)
#    else:
#        print getNumofmaxsq(Y, X)

print getNumofmaxsq(5, 16)
