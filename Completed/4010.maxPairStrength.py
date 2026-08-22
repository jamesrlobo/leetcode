# 4010. Maximize Pair Strength Using GCD
# https://leetcode.com/problems/maximize-pair-strength-using-gcd/description/
# Beats: 22.17%
import math


def maxPairStrength(nums):
    output = []
    n = len(nums)
    for i in range(n):
        for j in range(i+1, n):
            output.append((nums[i]*nums[j])//(math.gcd(nums[i], nums[j])**2))
    return max(output)


nums = [2,3,5]
nums = [4,6,8]
nums = [3,3]
print(maxPairStrength(nums))

# import math
#
#
# def maxPairStrength(nums):
#     output = []
#     n = len(nums)
#     for i in range(n):
#         for j in range(i+1, n):
#             output.append((nums[i]*nums[j])//(math.gcd(nums[i], nums[j])**2))
#     return max(output)
