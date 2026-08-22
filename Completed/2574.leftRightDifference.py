# 2574. Left and Right Sum Differences
# Beats: 69.11%
def leftRightDifference(nums):
    output = []
    leftSum = [0]
    temp1, temp2 = 0, 0
    for i in range(1, len(nums)):
        temp1 += nums[i-1]
        leftSum.append(temp1)
    rightSum = [0]
    nums = nums[::-1]
    for j in range(1, len(nums)):
        temp2 += nums[j-1]
        rightSum.append(temp2)
    rightSum = rightSum[::-1]
    # print(leftSum)
    # print(rightSum)
    for x, y in zip(leftSum, rightSum):
        output.append(abs(x-y))
    return output


nums = [10,4,8,3]
nums = [1]
print(leftRightDifference(nums))
