# 1450. Number of Students Doing Homework at a Given Time
# https://leetcode.com/problems/number-of-students-doing-homework-at-a-given-time/description/
# Beats: 100.00%
def busyStudent(startTime, endTime, queryTime):
    n = len(startTime)
    output = 0
    for i in range(n):
        if startTime[i] <= queryTime <= endTime[i]:
            output += 1
    return output

startTime = [1,2,3]
endTime = [3,2,7]
queryTime = 4
print(busyStudent(startTime, endTime, queryTime))
