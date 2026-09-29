# 1742. Maximum Number of Balls in a Box
# Beats: 56.30%
def countBalls(lowLimit, highLimit):
    d = {}
    for i in range(lowLimit, highLimit+1):
        if i < 10:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        else:
            temp = 0
            for j in str(i):
                temp += int(j)
            if temp in d:
                d[temp] += 1
            else:
                d[temp] = 1
    return max(d.values())


lowLimit = 1
highLimit = 10

lowLimit = 5
highLimit = 15

lowLimit = 19
highLimit = 28

lowLimit = 11
highLimit = 104

lowLimit = 220
highLimit = 548
print(countBalls(lowLimit, highLimit))
