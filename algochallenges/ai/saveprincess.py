def nextMove(n, r, c,p_r,p_c, grid):
    n_r = r
    n_c = c
    if r > p_r:
        n_r = r - 1
        print "UP"
    elif r < p_r:
        n_r = r + 1
        print "DOWN"
    elif c > p_c:
        n_c = c - 1
        print "LEFT"
    else:
        print "RIGHT"
        n_c = c + 1
    empty = '-'
    grid[r][c] = empty
    grid[n_r][n_c] = 'm'


def displayPathtoPrincess(n,grid):
    m_row = 0
    m_col = 0
    p_row = ""
    p_col = ""
    while m_row != p_row and m_col != p_col:
        for row_index, row in enumerate(grid):
            for column_index, cell in enumerate(row):
                if cell == 'm':
                    m_row = row_index
                    m_col = column_index
                if cell == 'p':
                    p_row = row_index
                    p_col = column_index
        nextMove(n, m_row, m_col, p_row , p_col,  grid)

grid = []

m = input()
for i in xrange(0, m):
    a = raw_input().strip()
    temp = []
    for j in a:
        temp.append(j)
    grid.append(temp)

displayPathtoPrincess(m, grid)