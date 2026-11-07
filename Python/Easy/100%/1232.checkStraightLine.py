# 1232. Check If It Is a Straight Line
# https://leetcode.com/problems/check-if-it-is-a-straight-line/description/
# Beats: 100.00%
def checkStraightLine(self, coordinates: list[list[int]]) -> bool:
    n = len(coordinates)
    if n == 2:
        return True
    (x0, y0) = coordinates[0]
    (x1, y1) = coordinates[1]
    dx = x1 - x0
    dy = y1 - y0
    for i in range(2, n):
        (xi, yi) = coordinates[i]
        if dx * (yi - y1) != dy * (xi - x1):
            return False
    return True
