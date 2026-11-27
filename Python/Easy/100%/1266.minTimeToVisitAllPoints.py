# 1266. Minimum Time Visiting All Points
# https://leetcode.com/problems/minimum-time-visiting-all-points/description/
# Beats: 100.00%
def minTimeToVisitAllPoints(self, points: list[list[int]]) -> int:
    n = len(points)
    output = 0
    for i in range(n-1):
        x1 = points[i][0]
        y1 = points[i][1]
        x2 = points[i+1][0]
        y2 = points[i+1][1]
        output += max(abs(x2-x1), abs(y2-y1))
    return output
