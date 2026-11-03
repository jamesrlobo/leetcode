# 1332. Remove Palindromic Subsequences
# https://leetcode.com/problems/remove-palindromic-subsequences/description/
# Beats:100.00%
def removePalindromeSub(self, s: str) -> int:
    if s == s[::-1]:
        return 1
    else:
        return 2
