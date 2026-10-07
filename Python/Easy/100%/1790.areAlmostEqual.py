# 1790. Check if One String Swap Can Make Strings Equal
# https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/
# Beats: 100.00%
def areAlmostEqual(self, s1: str, s2: str) -> bool:
    if s1 == s2:
        return True
    n = len(s1)
    count = 0
    diff = []
    for i in range(n):
        if s1[i] != s2[i]:
            count += 1
            diff.append([s1[i], s2[i]])
        if count > 2:
            return False
    if count != 0 and count != 2:
        return False
    if diff[0] == diff[1][::-1]:
        return True
    return False
