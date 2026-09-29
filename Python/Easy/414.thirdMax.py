# 414. Third Maximum Number
# https://leetcode.com/problems/third-maximum-number/description/
# Beats: 43.34%
def thirdMax(nums):
    if len(set(nums)) < 3:
        return max(nums)
    else:
        nums = sorted(set(nums))[::-1]
        return nums[2]


nums = [3,2,1]
nums = [1,2]
nums = [2,2,3,1]
print(thirdMax(nums))
