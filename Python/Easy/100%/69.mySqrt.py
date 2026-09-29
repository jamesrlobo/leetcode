# 69. Sqrt(x)
# https://leetcode.com/problems/sqrtx/description/
# Beats: 100.00%
def mySqrt(x):
    if x == 0:
        return 0
    first = 1
    last = x
    while first <= last:
        mid = first + (last-first)//2
        square = mid*mid
        if square == x:
            return mid
        elif square > x:
            last = mid-1
        elif square < x:
            first = mid+1
    return last


x = 4
x = 8
print(mySqrt(x))
