# 2639. Find the Width of Columns of a Grid
# Beats: 94.74%
def findColumnWidth(grid):
    output = []
    m = len(grid)
    n = len(grid[0])
    for i in range(n):
        l = 0
        for j in range(m):
            if len(str(grid[j][i])) > l:
                l = len(str(grid[j][i]))
        output.append(l)
    return output


# grid = [[-15,1,3],[15,7,12],[5,6,-2]]
grid = [[1],[22],[333]]
# grid = [[1]]
print(findColumnWidth(grid))

# def findColumnWidth(grid):
#     output = []
#     for i in range(len(grid)):
#         l = 0
#         for j in range(len(grid[i])):
#             if len(str(grid[j][i])) > l:
#                 l = len(str(grid[j][i]))
#         output.append(l)
#     return output
