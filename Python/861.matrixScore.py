# https://leetcode.com/problems/score-after-flipping-matrix/description/
# 861. Score After Flipping Matrix
def matrixScore(grid):
    print(grid)
    output = 0
    highest = len(grid[0]) * [1]
    while grid[0] != highest:
        for i in range(len(grid[0])):
            if grid[0][i] == 0:
                grid[0][i] = 1
            else:
                grid[0][i] = 0
        print(grid)
        for j in range(len(grid[0])):
            if grid[0][j] == 0:
                for k in grid:
                    if k[j] == 0:
                        k[j] = 1
                    else:
                        k[j] = 0
    print(grid)
    for row in grid:
        string = ""
        for value in row:
            string += str(value)
            print(string)
        output += int(string, 2)
        print(output)
    return grid, output


grid = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
grid = [[0]]
grid = [[0,1],[0,0]]
print(matrixScore(grid))
