# 415. Add Strings
# https://leetcode.com/problems/add-strings/description/
import sys

def addStrings(num1, num2):
    sys.set_int_max_str_digits(0)
    return str(int(num1)+int(num2))

num1 = "11"
num2 = "123"
print(addStrings(num1, num2))
