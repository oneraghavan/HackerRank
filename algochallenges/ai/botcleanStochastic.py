#!/usr/bin/python
def getClosestDirtyCell(board):
    for row_index, row in enumerate(board):
        for column_index, cell in enumerate(row):
            if cell == 'd':
                return row_index , column_index


def next_move(posr, posc,a,b, board):
    p_r, p_c = getClosestDirtyCell(board)
    if posr > p_r:
        print "UP"
    elif posr < p_r:
        print "DOWN"
    elif posc > p_c:
        print "LEFT"
    elif posc < p_c:
        print "RIGHT"
    else:
        print "CLEAN"
        
if __name__ == "__main__":
    pos = [int(i) for i in raw_input().strip().split()]
    dim = [int(i) for i in raw_input().strip().split()]
    board = [[j for j in raw_input().strip()] for i in range(dim[0])]
    next_move(pos[0], pos[1], dim[0], dim[1], board)
