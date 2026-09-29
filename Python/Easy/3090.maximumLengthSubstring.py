# 3090. Maximum Length Substring With Two Occurrences
# https://leetcode.com/problems/maximum-length-substring-with-two-occurrences/description/
# Beats: 5.04%
def maximumLengthSubstring(s):
    output = ""
    n = len(s)
    for i in range(n):
        for j in range(i, n+1):
            temp = s[i:j]
            for k in set(temp):
                if temp.count(k) > 2:
                    break
            else:
                if len(output) < len(temp):
                    output = temp
    return output


s = "bcbbbcba"
s = "aaaa"
print(maximumLengthSubstring(s))
