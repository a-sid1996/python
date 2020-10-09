# shit 2d array (LC 1260)

def shiftGrid(grid, k):
    q = []
    for i in grid:
        for j in i:
            q.append(j)

    k = k % ( len(q) )
    q = q[-k:] + q[:-k]
    
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            grid[i][j] = q.pop(0)
    return grid
    
grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]]
k = 4

print(shiftGrid(grid, k))
