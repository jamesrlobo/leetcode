# 136. Single Number
# https://leetcode.com/problems/single-number/
# Beats: 100.00%
def singleNumber(nums):
    output = 0
    for i in nums:
        output ^= i
    return output

nums = [2,2,1]
print(singleNumber(nums))
