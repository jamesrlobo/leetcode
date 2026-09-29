# 3442. Maximum Difference Between Even and Odd Frequency I
# Beats: 70.27%
def maxDifference(s):
    even, odd = [], []
    for i in set(s):
        if s.count(i)%2 == 0:
            even.append(s.count(i))
        else:
            odd.append(s.count(i))
    return max(odd) - min(even)


s = "aaaaabbc"
s = "abcabcab"
s = "mmsmsym"
print(maxDifference(s))
