# 3028. Ant on the Boundary
# Beats: 88.26%
def returnToBoundaryCount(nums):
    count, output = 0, 0
    for i in range(len(nums)):
        count += nums[i]
        if count == 0:
            output +=1
    return output


nums = [2,3,-5]
print(returnToBoundaryCount(nums))
