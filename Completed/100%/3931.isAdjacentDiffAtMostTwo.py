# 3931. Check Adjacent Digit Differences
# https://leetcode.com/problems/check-adjacent-digit-differences/description/
# Beats: 100.00%
def isAdjacentDiffAtMostTwo(s):
    n = len(s)
    for i in range(n-1):
        if abs(int(s[i]) - int(s[i+1])) > 2:
            return False
    return True


s = "132"
s = "129"
print(isAdjacentDiffAtMostTwo(s))
