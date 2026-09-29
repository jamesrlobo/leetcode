# 633. Sum of Square Numbers
# https://leetcode.com/problems/sum-of-square-numbers/description/
# Beats: 23.13%
import math


def judgeSquareSum(c):
    sqrt_c = int(math.sqrt(c)+1)
    print(sqrt_c)
    for i in range(sqrt_c):
        sqr_a = i**2
        sqr_b = c - sqr_a
        print(i, int(math.sqrt(sqr_b)))
        if sqr_a + int(math.sqrt(sqr_b))**2 == c:
            return True
    return False


c = 5
# c = 3
# c = 4
c = 8
print(judgeSquareSum(c))

# TLE
# def judgeSquareSum(c):
#     c_sqrt = int(math.sqrt(c))
#     # print(c_sqrt)
#     for i in range(0, c_sqrt+1):
#         for j in range(c_sqrt+1, 0, -1):
#             if ((i**2)+(j**2)) == c:
#                 return True
#     return False
