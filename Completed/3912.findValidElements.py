# 3912. Valid Elements in an Array
# https://leetcode.com/problems/valid-elements-in-an-array/description/
# Beats: 13.37%
def findValidElements(nums):
    if len(nums) == 1:
        return nums
    output = [nums[0]]
    for i in range(1, len(nums)-1):
        if nums[i] > max(nums[:i]):
            # print(nums[i], max(nums[:i]))
            output.append(nums[i])
            # print(output)
        elif nums[i] > max(nums[i+1:]):
            # print(nums[i], max(nums[i:]))
            output.append(nums[i])
            # print(output)
    output.append(nums[-1])
    return output


nums = [1,2,4,2,3,2]
nums = [5,5,5,5]
nums = [1, 1]
print(findValidElements(nums))
