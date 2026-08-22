# 1979. Find Greatest Common Divisor of Array
# https://leetcode.com/problems/find-greatest-common-divisor-of-array/
# Beats: 100.00%
import math


def findGCD(nums):
    return math.gcd(max(nums), min(nums))


nums = [2,5,6,9,10]
print(findGCD(nums))
