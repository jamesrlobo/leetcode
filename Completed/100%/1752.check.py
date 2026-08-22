# 1752. Check if Array Is Sorted and Rotated
# https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/description/
# Beats: 100.00%
def check(nums):
    if nums == sorted(nums):
        return True
    n = len(nums)
    for i in range(n):
        if nums[i] == min(nums):
            temp = (nums[i:] + nums[:i])
            if temp == sorted(temp):
                return True
    return False


nums = [3,4,5,1,2]
nums = [2,1,3,4]
nums = [1,2,3]
nums = [6,10,6]
print(check(nums))


# def check(self, nums: List[int]) -> bool:
#     if nums == sorted(nums):
#         return True
#     for i in range(len(nums)):
#         temp = nums[i:len(nums)] + nums[:i]
#         if temp ==  sorted(nums):
#             return True
#     return False
