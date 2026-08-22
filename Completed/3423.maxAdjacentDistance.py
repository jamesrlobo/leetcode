# 3423. Maximum Difference Between Adjacent Elements in a Circular Array
# Beats: 48.34%
def maxAdjacentDistance(nums):
    output = []
    for i in range(len(nums)):
        output.append(abs(nums[i-1] - nums[i]))
    return max(output)


nums = [1,2,4]
nums = [-5,-10,-5]
print(maxAdjacentDistance(nums))
