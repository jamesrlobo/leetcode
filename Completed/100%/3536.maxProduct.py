# 3536. Maximum Product of Two Digits
# https://leetcode.com/problems/maximum-product-of-two-digits/
# Beats: 100.00%
def maxProduct(n):
    nums = [int(x) for x in str(n)]
    nums = sorted(nums, reverse=True)
    return nums[0] * nums[1]


# n = 31
# n = 22
n = 124
print(maxProduct(n))
