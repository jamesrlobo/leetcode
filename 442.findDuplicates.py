# 442. Find All Duplicates in an Array
# https://leetcode.com/problems/find-all-duplicates-in-an-array/
def findDuplicates(nums):
    n = len(nums)
    print(nums)
    for i in range(n):
        temp = nums[i]
        val = nums[temp-1]
        nums[temp-1] = -(val)
        print(nums)
    return nums


nums = [4,3,2,7,8,2,3,1]
nums = [2,5,2,1,1,4]
print(findDuplicates(nums))
