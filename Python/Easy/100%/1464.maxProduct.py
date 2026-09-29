# 1464. Maximum Product of Two Elements in an Array
# https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/description/
# Beats: 100.00%
def maxProduct(nums):
    nums.sort()
    max1 = nums[-1]
    max2 = nums[-2]
    return ((max1-1) * (max2-1))


nums = [3,4,5,2]
nums = [1,5,4,5]
nums = [3,7]
print(maxProduct(nums))

# output = 0
# n = len(nums)
# for i in range(n):
#     for j in range(i, n):nums[i
#         if i != j:
#             output = max((nums[i]-1)*(nums[j]-1), output)
# return output
