# 561. Array Partition
# Beats: 5.12%
def arrayPairSum(nums):
    maxSum = 0
    nums = sorted(nums)
    while len(nums) > 0:
        maxSum += (min(nums[0], nums[1]))
        nums = nums[2:]
    return maxSum


nums = [1,4,3,2]
# nums = [6,2,6,5,1,2]
print(arrayPairSum(nums))
