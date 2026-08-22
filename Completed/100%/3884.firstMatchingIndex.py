# 3884. First Matching Character From Both Ends
# Beats: 100.00%
def firstMatchingIndex(s):
    n = len(s)
    for i in range(len(s)):
        if s[i] == s[n-i-1]:
            return i
    return -1


s = "abcacbd"
s = "abc"
s = "abcdab"
print(firstMatchingIndex(s))
