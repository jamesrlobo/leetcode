# 1403. Minimum Subsequence in Non-Increasing Order
# https://leetcode.com/problems/minimum-subsequence-in-non-increasing-order/description/
# Beats: 16.03%
def minSubsequence(nums):
    if len(nums) == 1:
        return nums
    nums = sorted(nums)[::-1]
    print(nums)
    for i in range(1, len(nums)):
        if sum(nums[:i]) > sum(nums[i:]):
            return nums[:i]
    return nums


# nums = [4,3,10,9,8]
# nums = [4,4,7,6,7]
nums = [6,4,4,7,7]
nums = [6]
nums = [8,8]
print(minSubsequence(nums))
