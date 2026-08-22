# 2405. Optimal Partition of String
# https://leetcode.com/problems/optimal-partition-of-string/description/
# Beats: 96.19%
def partitionString(s):
    output = []
    n = len(s)
    temp = ""
    for i in range(n):
        # print(s[i])
        if s[i] not in temp:
            temp += s[i]
        else:
            output.append(temp)
            temp = s[i]
    output.append(temp)
    return len(output)


s = "abacaba"
s = "ssssss"
print(partitionString(s))
