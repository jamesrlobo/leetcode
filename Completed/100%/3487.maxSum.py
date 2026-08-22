# https://leetcode.com/problems/maximum-unique-subarray-sum-after-deletion/description/
# 3487. Maximum Unique Subarray Sum After Deletion
# Beats: 100.00%
def maxSum(nums):
    if max(nums) < 0:
        return max(nums)
    output = 0
    temp = list(set(nums))
    for i in temp:
        if i >= 0:
            output += i
    return output


nums = [1,1,0,1,1]
nums = [1,2,-1,-2,1,0,-1]
nums = [-100]
print(maxSum(nums))
