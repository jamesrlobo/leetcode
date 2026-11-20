# 812. Largest Triangle Area
# https://leetcode.com/problems/largest-triangle-area/description/
# Beats: 23.05%
def largestTriangleArea(self, points: list[list[int]]) -> float:
    n = len(points)
    result = []
    for i in range(n-2):
        for j in range(i, n-1):
            for k in range(j, n):
                if i != j != k:
                    # print(points[i], points[j], points[k])
                    x1, y1 = points[i][0], points[i][1]
                    x2, y2 = points[j][0], points[j][1]
                    x3, y3 = points[k][0], points[k][1]
                    area = 0.5 * abs((x1 * (y2-y3))+ (x2 * (y3-y1)) + (x3 * (y1-y2)))
                    result.append(area)
    return max(result)
