# 4070. Minimum Rotations to Dial a Number I
# https://leetcode.com/problems/minimum-rotations-to-dial-a-number-i/description/
# Beats: 100.00%
def minRotations(self, s: str) -> int:
    n = len(s)
    rotations, curr = 0, 0
    for i in range(n):
        d = abs(curr - int(s[i]))
        rotations += min(d, 10-d)
        curr = int(s[i])
    return rotations
