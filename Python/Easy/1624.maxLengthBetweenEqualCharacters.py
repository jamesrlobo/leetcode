# 1624. Largest Substring Between Two Equal Characters
# https://leetcode.com/problems/largest-substring-between-two-equal-characters/description/
# Beats: 34.40%
def maxLengthBetweenEqualCharacters(s):
    output = []
    for i in set(s):
        if s.count(i) > 1:
            temp = []
            for j in range(len(s)):
                if i == s[j]:
                    temp.append(j)
            output.append(len(s[min(temp)+1:max(temp)]))
    if output:
        return max(output)
    return -1


s = "aa"
# s = "abca"
s = "cbzxy"
print(maxLengthBetweenEqualCharacters(s))
