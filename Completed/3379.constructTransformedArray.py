# 3379. Transformed Array
# Beats:92.61%
def constructTransformedArray(nums):
    result = []
    n = len(nums)
    for i in range(len(nums)):
        if nums[i] == 0:
            result.append(nums[i])
        elif nums[i] > 0:
            if i + abs(nums[i]) >= n:
                result.append(nums[(i+abs(nums[i]))%n])
            else:
                result.append(nums[i+abs(nums[i])])
        elif nums[i] < 0:
            if i + abs(nums[i]) >= n:
                result.append(nums[(i-abs(nums[i]))%n])
            else:
                result.append((nums[i-abs(nums[i])]))
    return result


# nums = [3,-2,1,1]
# nums = [-1,4,-1]
nums = [-10]
print(constructTransformedArray(nums))
