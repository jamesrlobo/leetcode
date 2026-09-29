# 2224. Minimum Number of Operations to Convert Time
# https://leetcode.com/problems/minimum-number-of-operations-to-convert-time/description/
# Beats: 100.00%
def convertTime(current, correct):
    current = current.split(":")
    time1 = (int(current[0]) * 60)+int(current[1])
    correct = correct.split(":")
    time2 = (int(correct[0]) * 60)+int(correct[1])
    count = 0
    while time1 != time2:
        if (time2 - time1) >= 60:
            time1 += 60
        elif (time2 - time1) >= 15:
            time1 += 15
        elif (time2 - time1) >= 5:
            time1 += 5
        elif (time2 - time1) >= 1:
            time1 += 1
        count += 1
    return count


current = "02:30"
correct = "04:35"
print(convertTime(current, correct))
