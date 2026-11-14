# 3402. Minimum Operations to Make Columns Strictly Increasing
# https://leetcode.com/problems/minimum-operations-to-make-columns-strictly-increasing/description/
# Beats: 21.77%
def minimumOperations(self, grid: List[List[int]]) -> int:
    output = 0
    for i in range(1, len(grid)):
        for j in range(len(grid[i])):
            if grid[i-1][j] >= grid[i][j]:
                temp = grid[i-1][j] - grid[i][j] + 1
                output += temp
                grid[i][j] += temp
    return output
