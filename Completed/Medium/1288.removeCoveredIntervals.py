# 1288. Remove Covered Intervals
# https://leetcode.com/problems/remove-covered-intervals/description
# Beats: 77.50%
def removeCoveredIntervals(intervals):
    intervals = sorted(intervals)
    print(intervals)
    n = len(intervals)
    i = 0
    while i < (len(intervals)-1):
        if(intervals[i+1][0] >= intervals[i][0] and intervals[i][1] >= intervals[i+1][1]):
            intervals.pop(i+1)
        elif intervals[i][0] >= intervals[i+1][0] and intervals[i+1][1] >= intervals[1][1]:
            intervals.pop(i)
        else:
            i+=1
    return len(intervals)


intervals = [[1,4],[3,6],[2,8]]
intervals = [[1,4],[2,3]]
intervals = [[3,10],[4,10],[5,11]]
intervals = [[1,2],[1,4],[3,4]]
print(removeCoveredIntervals(intervals))
