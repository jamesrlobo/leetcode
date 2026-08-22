# 2996. Smallest Missing Integer Greater Than Sequential Prefix Sum
# https://leetcode.com/problems/smallest-missing-integer-greater-than-sequential-prefix-sum/description/
# Beats: 100.00%
def missingInteger(nums):
    n = len(nums)
    i = 1
    seq = nums[0]
    while i < n:
        # print(nums[i])
        if nums[i] == nums[i-1] + 1:
            seq += nums[i]
            i+=1
        else:
            break
    if seq not in nums:
        return seq
    else:
        for j in range(seq, max(nums)+2):
            if j not in nums:
                return j



# nums = [1,2,3,2,5]
nums = [3,4,5,1,12,14,13]
# nums = [29,30,31,32,33,34,35,36,37]
print(missingInteger(nums))
