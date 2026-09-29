# 2903. Find Indices With Index and Value Difference I
# Beats: 48.88%
def findIndices(nums, indexDifference, valueDifference):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if abs(i-j) >= indexDifference and abs(nums[i]- nums[j]) >= valueDifference:
                return [i,j]
    return [-1,-1]


# nums = [5,1,4,1]
# indexDifference = 2
# valueDifference = 4

# nums = [2,1]
# indexDifference = 0
# valueDifference = 0

nums = [1,2,3]
indexDifference = 2
valueDifference = 4
print(findIndices(nums, indexDifference, valueDifference))
