# 2437. Number of Valid Clock Times
# Beats: 100.00%
import math


def countTime(time):
    output = []
    time = time.split(":")
    # print(time[0])
    if time[0] == "??":
        output.append(24)
    elif time[0][0] == "?":
        if int(time[0][1]) > 3:
            output.append(2)
        else:
            output.append(3)
    elif time[0][1] == "?":
        if int(time[0][0]) <= 1:
            output.append(10)
        else:
            output.append(4)
    # print(time[1])
    if time[1] == "??":
        output.append(60)
    elif time[1][0] == "?":
        output.append(6)
    elif time[1][1] == "?":
        output.append(10)
    return math.prod(output)


time = "?5:00"
time = "0?:0?"
time = "??:??"
time = "?2:16"
time = "2?:??"
print(countTime(time))


# https://leetcode.com/problems/latest-time-by-replacing-hidden-digits/description/
