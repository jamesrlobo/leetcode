# 3127. Make a Square with the Same Color
# https://leetcode.com/problems/make-a-square-with-the-same-color/
# Beats: 100.00%
def canMakeSquare(self, grid: List[List[str]]) -> bool:
    top_right = grid[0][0:2] + grid[1][0:2]
    if top_right.count("W") >= 3 or top_right.count("B") >= 3:
        return True
    top_left = grid[0][1:] + grid[1][1:]
    if top_left.count("W") >= 3 or top_left.count("B") >= 3:
        return True
    bottom_right = grid[1][0:2] + grid[2][0:2]
    if bottom_right.count("W") >= 3 or bottom_right.count("B") >= 3:
        return True
    bottom_left = grid[1][1:] + grid[2][1:]
    if bottom_left.count("W") >= 3 or bottom_left.count("B") >= 3:
        return True
    return False
