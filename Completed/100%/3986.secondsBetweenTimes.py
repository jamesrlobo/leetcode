# 3986. Number of Elapsed Seconds Between Two Times
# https://leetcode.com/problems/number-of-elapsed-seconds-between-two-times/description/
# Beats: 100.00%
def secondsBetweenTimes(startTime, endTime):
    startTime = startTime.split(":")
    startTimeSeconds = int(startTime[0]) * 60 * 60 + int(startTime[1]) * 60 + int(startTime[2])
    endTime = endTime.split(":")
    endTimeSeconds = int(endTime[0]) * 60 * 60 + int(endTime[1]) * 60 + int(endTime[2])
    return endTimeSeconds - startTimeSeconds


startTime = "01:00:00"
endTime = "01:00:25"

startTime = "12:34:56"
endTime = "13:00:00"
print(secondsBetweenTimes(startTime, endTime))
