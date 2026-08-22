# 3760. Maximum Substrings With Distinct Start
# Beats: 98.13%
def maxDistinct(s):
    return len(set(s))


s = "abab"
print(maxDistinct(s))
