# 2873. Maximum Value of an Ordered Triplet I
# https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-i/
# Beats: 33.17%
def maximumTripletValue(nums):
    n = len(nums)
    tripletValue = []
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                temp_tripletValue = ((nums[i] - nums[j]) * nums[k])
                if temp_tripletValue >= 0:
                    tripletValue.append(temp_tripletValue)
    if len(tripletValue) > 0:
        return max(tripletValue)
    return 0


nums = [12,6,1,2,7]
nums = [1,10,3,4,19]
nums = [1,2,3]
print(maximumTripletValue(nums))
