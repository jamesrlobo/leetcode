# 3978. Unique Middle Element
# https://leetcode.com/problems/unique-middle-element/description/
# Beats: 100.00%
def isMiddleElementUnique(nums):
    mid = nums[len(nums)//2]
    if nums.count(mid) > 1:
        return False
    return True


nums = [1,2,3]
print(isMiddleElementUnique(nums))
