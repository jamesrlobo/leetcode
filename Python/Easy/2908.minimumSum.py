# 2908. Minimum Sum of Mountain Triplets I
# Beats: 5.58%
def minimumSum(nums):
    output = []
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            for k in range(j, len(nums)):
                if i < j and j < k:
                    if nums[i] < nums[j] and nums[j] > nums[k]:
                        output.append(nums[i] + nums[j] + nums[k])
    if len(output) > 0:
        return min(output)
    return -1


# nums = [8,6,1,5,3]
# nums = [5,4,8,7,10,2]
nums = [6,5,4,3,4,5]
print(minimumSum(nums))
