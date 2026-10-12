# 4056. Number of Intersecting Interval Pairs I
# https://leetcode.com/problems/number-of-intersecting-interval-pairs-i/
# Beats: 5.76%
def countIntersectingIntervals(self, intervals: list[list[int]]) -> int:
    n = len(intervals)
    output = 0
    for i in range(n):
        for j in range(i, n):
            if i < j:
                if max(intervals[i][0], intervals[j][0]) <= min(intervals[i][1], intervals[j][1]):
                    output += 1
    return output
