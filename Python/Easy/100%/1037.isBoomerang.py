# 1037. Valid Boomerang
# https://leetcode.com/problems/valid-boomerang/description/
# Beats: 100.00%
def isBoomerang(points):
    x1 = points[0][0]
    y1 = points[0][1]
    x2 = points[1][0]
    y2 = points[1][1]
    x3 = points[2][0]
    y3 = points[2][1]
    return (y2 - y1) * (x3 - x2) != (y3 - y2) * (x2 - x1)



points = [[1,1],[2,3],[3,2]]
points = [[1,1],[2,2],[3,3]]
print(isBoomerang(points))
