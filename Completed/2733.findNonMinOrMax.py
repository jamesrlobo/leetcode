# 2733. Neither Minimum nor Maximum
# https://leetcode.com/problems/neither-minimum-nor-maximum/description/
# Beats: 91.37%
def findNonMinOrMax(nums):
    mx = max(nums)
    mn = min(nums)
    for i in nums:
        if i != mx and i != mn:
            return i
    return -1


nums = [3,2,1,4]
nums = [1,2]
nums = [2,1,3]
print(findNonMinOrMax(nums))

# def findNonMinOrMax(nums):
#     nums = sorted(nums)
#     return nums[1]
