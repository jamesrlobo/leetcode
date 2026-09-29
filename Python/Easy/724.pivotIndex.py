# 724. Find Pivot Index
# Beats: 87.35%
def pivotIndex(nums):
    preSum = 0
    postSum = sum(nums)
    for i in range(len(nums)):
        postSum -= nums[i]
        if preSum == postSum:
            return i
        preSum += nums[i]
    return -1


nums = [1,7,3,6,5,6]
nums = [1,2,3]
nums = [2,1,-1]
print(pivotIndex(nums))
