# 4092. Binary Digit Score
# https://leetcode.com/problems/binary-digit-score/description/
# Beats: 17.11%
def calculateScore(self, a: int, b: int) -> int:
    a = bin(a)[2:]
    s1 = a.count('1')
    b = bin(b)[2:]
    s2 = b.count('1')
    if s1 >= s2:
        return int(s1*s2)
    else:
        return int(s2/s1)
