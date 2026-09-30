# 1111. Maximum Nesting Depth of Two Valid Parentheses Strings
# https://leetcode.com/problems/maximum-nesting-depth-of-two-valid-parentheses-strings/
# Beats: 46.30%
def maxDepthAfterSplit(seq):
    result = []
    d = 0
    for ch in seq:
        if ch == "(":
            d += 1
            result.append(d%2)
        if ch == ")":
            result.append(d%2)
            d -= 1
    return result

seq = "(()())"
print(maxDepthAfterSplit(seq))
