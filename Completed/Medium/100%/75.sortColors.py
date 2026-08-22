# 75. Sort Colors
# https://leetcode.com/problems/sort-colors/description/
# Beats: 100.00%
def sortColors(nums):
    l = len(nums)
    for i in set(nums):
        for j in range(nums.count(i)):
            nums.append(i)
    del nums[:l]
    return nums


nums = [2,0,2,1,1,0]
# nums = [2,0,1]
# nums = [0,1,2]
print(sortColors(nums))
