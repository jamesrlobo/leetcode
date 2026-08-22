# 2319. Check if Matrix Is X-Matrix
def checkXMatrix(grid):
    n = len(grid)
    primary_diagonal, secondary_diagonal = [], []
    for i in range(n):
        if grid[i][i] == 0:
            return False
        else:
            primary_diagonal.append(grid[i][i])
    for j in range(n):
        if grid[j][(n-1)-j] == 0:
            return False
        else:
            secondary_diagonal.append(grid[j][(n-1)-j])
    for x in range(n):
        for y in range(n):
            if x != y and (x != n -1 -y):
                if grid[x][y] != 0:
                    return False
    return True


grid = [[2,0,0,1],[0,3,1,0],[0,5,2,0],[4,0,0,2]]
print(checkXMatrix(grid))
