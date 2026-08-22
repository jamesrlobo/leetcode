# 9. Palindrome Number
# https://leetcode.com/problems/palindrome-number/
# Beats: 90.85%
def isPalindrome(x):
    x = str(x)
    rev_x = x[::-1]
    if x == rev_x:
        return True
    return False

x = 121
x = -121
x = 10
print(isPalindrome(x))
