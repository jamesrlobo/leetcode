# 162. Find Peak Element
# https://leetcode.com/problems/find-peak-element/description/
# Beats: 100.00%
def findPeakElement(nums):
    n = len(nums)
    for i in range(1, n-1):
        if nums[i-1] < nums[i] and nums[i] > nums[i+1]:
            return i
    # print(nums[-2], nums[-1])
    if nums[-2] < nums[-1]:
        return n-1
    return 0


nums = [1,2,3,1]
nums = [1,2]
print(findPeakElement(nums))
