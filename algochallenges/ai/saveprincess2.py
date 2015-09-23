#!/bin/python
def nextMove(n,r,c,grid):
    p_r = ""
    p_r = ""
    for row_index , row in enumerate(grid):
        for column_index,cell in enumerate(row):
            if cell == 'p':
                p_r = row_index
                p_c = column_index
    if r > p_r:
        return "UP"
    elif r < p_r:
            return "DOWN"
    elif c > p_c:
        return "LEFT"
    else:
        return "RIGHT"

n = input()
r,c = [int(i) for i in raw_input().strip().split()]
grid = []
for i in xrange(0, n):
    grid.append(raw_input())

print nextMove(n,r,c,grid)




