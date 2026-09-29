# 3731. Find Missing Elements
# Beats: 100.00%
def findMissingElements(nums):
    output = []
    minimum = min(nums)
    maximum = max(nums)
    for i in range(minimum, maximum+1):
        if i not in nums:
            output.append(i)
    return output


# nums = [1,4,2,5]
# nums = [7,8,6,9]
nums = [5,1]
print(findMissingElements(nums))
