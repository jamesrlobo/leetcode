# 3264. Final Array State After K Multiplication Operations I
def getFinalState(nums, k, multiplier):
    for i in range(k):
        minimum = min(nums)
        for j in range(len(nums)):
            if nums[j] == minimum:
                nums[j] = nums[j] * multiplier
                break
    return nums


# nums = [2,1,3,5,6]
# k = 5
# multiplier = 2
nums = [1,2]
k = 3
multiplier = 4
print(getFinalState(nums, k, multiplier))
