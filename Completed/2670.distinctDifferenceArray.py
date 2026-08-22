# 2670. Find the Distinct Difference Array
# Beats: 84.59%
def distinctDifferenceArray(nums):
    output = []
    for i in range(len(nums)):
        # print(len(set(nums[:i+1])), len(set(nums[i+1:])))
        output.append(len(set(nums[:i+1])) - len(set(nums[i+1:])))
    return output


# nums  = [1,2,3,4,5]
nums = [3,2,3,4,2]
print(distinctDifferenceArray(nums))
