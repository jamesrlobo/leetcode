# 2496. Maximum Value of a String in an Array
# https://leetcode.com/problems/maximum-value-of-a-string-in-an-array/description/
# Beats: 100.00%
def maximumValue(strs):
    val = 0
    for s in strs:
        if s.isdigit():
            val = max(val, int(s))
        elif s.isalnum():
            val = max(val, len(s))
        print(s, val)
    return val


# strs = ["alic3","bob","3","4","00000"]
# strs = ["1","01","001","0001"]
print(maximumValue(strs))
