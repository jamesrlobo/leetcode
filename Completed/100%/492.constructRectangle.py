# https://leetcode.com/problems/construct-the-rectangle/description/
# 492. Construct the Rectangle
# Beats: 100.00%
import math
def constructRectangle(area):
    l = 0
    w = int(math.sqrt(area))
    while area%w != 0:
        w -=1
    l = area//w
    return [l, w]


area = 4
area = 37
area = 122122
print(constructRectangle(area))
