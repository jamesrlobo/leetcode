# 1614. Maximum Nesting Depth of the Parentheses
# https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/
# Beats: 100.00%
def maxDepth(s):
    n = len(s)
    result = []
    for i in range(n):
        result.append(s[:i].count("(") - s[:i].count(")"))
    if result:
        return max(result)
    return 0


s = "(1)+((2))+(((3)))"
s = "(1+(2*3)+((8)/4))+1"
print(maxDepth(s))
