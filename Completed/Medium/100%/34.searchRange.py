# 34. Find First and Last Position of Element in Sorted Array
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
# Beats: 100.00%
def searchRange(nums, target):
    minimum = -1
    maximum = -1
    if nums.count(target) == 1:
        return [nums.index(target), nums.index(target)]
    for i in range(len(nums)):
        if nums[i] == target and minimum != -1:
            maximum = i
        elif nums[i] == target and minimum == -1:
            minimum = i
    return [minimum, maximum]


# nums = [5,7,7,8,8,10]
# target = 8
# nums = [5,7,7,8,8,10]
# target = 6
nums = [1]
target = 1
print(searchRange(nums, target))
