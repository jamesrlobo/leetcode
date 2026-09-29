# 1. Two Sum
# https://leetcode.com/problems/two-sum/description/
# Beats: 30.98%
def twoSum(nums, target):
    for i in range(len(nums)):
        temp = target - nums[i]
        if temp in nums and i != nums.index(temp):
            return [i, nums.index(temp)]


nums = [2,7,11,15]
target = 9
nums = [3,2,4]
target = 6
nums = [3,3]
target = 6
print(twoSum(nums, target))
