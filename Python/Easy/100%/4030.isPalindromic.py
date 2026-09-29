# 4030. Check ASCII Palindromic
# https://leetcode.com/problems/check-ascii-palindromic/description/
# Beats: 100.00%
def isPalindromic(s):
    output = ""
    for i in s:
        output += (bin(ord(i))[2:]).zfill(8)
    return output == output[::-1]


s = "ff"
s = "leet"
print(isPalindromic(s))
