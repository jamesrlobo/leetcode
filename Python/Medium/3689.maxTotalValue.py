# 3689. Maximum Total Subarray Value I
# https://leetcode.com/problems/maximum-total-subarray-value-i/description/
# Beats: 80.80%
def maxTotalValue(nums, k):
    global_max = max(nums)
    global_min = min(nums)
    return (global_max - global_min)*k


nums = [1,3,2]
k = 2
nums = [4,2,5,1]
k = 3
nums = [11,8]
k = 2
print(maxTotalValue(nums, k))

# def maxTotalValue(nums, k):
#     values = 0
#     n = len(nums)
#     for i in range(n):
#         for j in range(i, n+1):
#             if len(nums[i:j]) > 0:
#                 temp = nums[i:j]
#                 val = max(temp) - min(temp)
#                 if val >= values:
#                     values = val
#     return values*k
