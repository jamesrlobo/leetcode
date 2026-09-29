# 3908. Valid Digit Number
# https://leetcode.com/problems/valid-digit-number/description/
# Beats: 100.00%
def validDigit(n, x):
    n = list(str(n))
    print(n)
    if n[0] == str(x) or n.count(str(x)) == 0:
        return False
    return True


n = 101
x = 0

n = 232
x = 2
print(validDigit(n, x))
