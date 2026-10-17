# 4074. Maximum Product Pair With Target Sum
# https://leetcode.com/problems/maximum-product-pair-with-target-sum/
# Beats: 23.85%
def maxProductPair(self, nums: list[int], target: int) -> list[int]:
    d = {}
    n = len(nums)
    for i in range(n):
        for j in range(n):
            if i != j:
                if nums[i] > nums[j] and (nums[i] + nums[j]) == target:
                    d[i,j] = nums[i]*nums[j]
    if len(d) == 0:
        return [-1, -1]
    return max(d, key=d.get)
