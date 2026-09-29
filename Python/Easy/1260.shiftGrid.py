# 1260. Shift 2D Grid
# https://leetcode.com/problems/shift-2d-grid/description/?envType=daily-question&envId=2026-07-20
# Beats: 85.39%
def shiftGrid(grid, k):
    final = []
    m = len(grid[0])
    for i in range(len(grid)):
        final.extend(grid[i])
    for j in range(k):
        temp = final.pop()
        final.insert(0, temp)
    x = 0
    grid = []
    while x < len(final)-m+1:
        grid.append(final[x:x+m])
        x += m
    return grid


grid = [[1,2,3],[4,5,6],[7,8,9]]
k = 1
grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]]
k = 4
print(shiftGrid(grid, k))
