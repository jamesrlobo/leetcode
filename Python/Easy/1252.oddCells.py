# 1252. Cells with Odd Values in a Matrix
# https://leetcode.com/problems/cells-with-odd-values-in-a-matrix/
# Beats: 17.83%
def oddCells(self, m: int, n: int, indices: list[list[int]]) -> int:
    grid = []
    for i in range(m):
        grid.append([0] * n)
    # print(grid)
    for ind in indices:
        # print("Row to manipulate:", grid[ind[0]])
        for x in range(n):
            grid[ind[0]][x] += 1
        # print("Col to manipulate:", ind[1])
        for y in range(m):
            grid[y][ind[1]] += 1
        # print(grid)
    output = 0
    for j in range(m):
        for k in grid[j]:
            if k%2 != 0:
                output += 1
    return output
