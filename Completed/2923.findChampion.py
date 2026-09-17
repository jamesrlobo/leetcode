# 2923. Find Champion I
# https://leetcode.com/problems/find-champion-i/description/
# Beats: 29.72%
def findChampion(grid):
    champ = 0
    for i in range(1, len(grid)):
        if grid[champ].count(1) < grid[i].count(1):
            champ = i
    return champ


grid = [[0,1],[0,0]]
grid = [[0,0,1],[1,0,1],[0,0,0]]
print(findChampion(grid))
