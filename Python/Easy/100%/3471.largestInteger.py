# 3471. Find the Largest Almost Missing Integer
# https://leetcode.com/problems/find-the-largest-almost-missing-integer/description/
# Beats: 100.00%
def largestInteger(nums, k):
    n = len(nums)
    if k == n:
        return max(nums)
    if k == 1:
        for i in sorted(set(nums), reverse=True):
            if nums.count(i) == 1:
                return i
    if k < n:
        output = []
        if nums.count(nums[0]) == 1:
            output.append(nums[0])
        if nums.count(nums[n-1]) == 1:
            output.append(nums[n-1])
        if output:
            return max(output)
    return -1


nums = [3,9,2,1,7]
k = 3

nums = [3,9,7,2,1,7]
k = 4

nums = [0,0]
k = 1
print(largestInteger(nums, k))

# def largestInteger(nums, k):
#     #create a list of subarrays
#     subarrays = []
#     i, j = 0, k
#     while i < len(nums):
#         if len(nums[i:j]) == k:
#             subarrays.append(nums[i:j])
#         i+=1
#         j+=1
#     print(subarrays)
#     #check for item in nums, count in subarray
#     output = []
#     for item in set(nums):
#         count = 0
#         for subarray in subarrays:
#             if item in subarray:
#                 count += 1
#         if count == 1:
#             output.append(item)
#     if len(output) == 0:
#         return -1
#     return max(output)
