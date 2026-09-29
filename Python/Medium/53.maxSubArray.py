# 53. Maximum Subarray (Copied from Solutions)
# Beats: 42.27%
def maxSubArray(nums):
    maxSum = nums[0]
    currSum = nums[0]
    for num in nums[1:]:
        currSum = max(num, currSum+num)
        maxSum = max(maxSum, currSum)
    return maxSum


nums = [-2,1,-3,4,-1,2,1,-5,4]
# nums = [1]
# nums = [5,4,-1,7,8]
# nums = [-1]
print(maxSubArray(nums))
