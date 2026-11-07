# 1854. Maximum Population Year
# https://leetcode.com/problems/maximum-population-year/description/
# Beats: 17.59%
def maximumPopulation(logs):
    d = {}
    for log in logs:
        for i in range(log[0],log[1]):
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
    maxVal = max(d.values())
    output = []
    for i in d:
        if d[i] == maxVal:
            output.append(i)
    return min(output)


logs = [[1993,1999],[2000,2010]]
# logs = [[1950,1961],[1960,1971],[1970,1981]]
print(maximumPopulation(logs))
