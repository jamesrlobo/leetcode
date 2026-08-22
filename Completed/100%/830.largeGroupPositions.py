# 830. Positions of Large Groups
# Beats: 100.00%
def largeGroupPositions(s):
    if len(set(s)) == 1 and len(s)-1 != 0 and len(s) > 3:
        return [[0,len(s)-1]]
    s += "0"
    output = []
    start = 0
    for i in range(len(s)-1):
        if s[i] != s[i+1]:
            if abs((start-1) - i) >= 3:
                output.append([start, i])
            start = i+1
    return output

s = "abbxxxxzzy"
s = "abc"
s = "abcdddeeeeaabbbcd"
s = "aaa"
s = "babaaaabbb"
s = "aa"
print(largeGroupPositions(s))
