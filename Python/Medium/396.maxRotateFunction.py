# 396. Rotate Function
# https://leetcode.com/problems/rotate-function/description/
# Beats: 59.79% (Help from solution)
def maxRotateFunction(nums):
    n = len(nums)
    total_sum = sum(nums)
    F = sum(i * nums[i] for i in range(n))
    ans = F
    for k in range(1, n):
        F = F + total_sum - n * nums[n-k]
        ans = max(ans, F)
    return ans

nums = [4,3,2,6]
nums = [100]
print(maxRotateFunction(nums))

# def maxRotateFunction(nums):
#     final_output = []
#     def f(nums, i):
#         output = 0
#         temp = nums[i:] + nums[:i]
#         # print(temp)
#         for x in range(len(temp)):
#             output += (x * temp[x])
#         return output
#     l = len(nums)
#     for i in range(l):
#         final_output.append(f(nums, i))
#     return max(final_output)
