# 2089. Find Target Indices After Sorting Array
#Runtime: 100%
def targetIndices(nums, target):
    output = []
    nums.sort()
    for i in range(len(nums)):
        if nums[i] == target:
            output.append(i)
    return output


# nums = [1,2,5,2,3]
# target = 2
# nums = [1,2,5,2,3]
# target = 3
nums = [1,2,5,2,3]
target = 5
print(targetIndices(nums, target))
