# 796. Rotate String
# https://leetcode.com/problems/rotate-string/description/
# Beats: 100.00%
def rotateString(s, goal):
    for i in range(len(s)):
        if (s[i:] + s[:i]) == goal:
            return True
    return False


s = "abcde"
goal = "cdeab"
print(rotateString(s, goal))
